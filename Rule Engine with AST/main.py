import streamlit as st
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
import sqlite3
import json

# Initialize FastAPI app
app = FastAPI()

# Configure CORS for cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite setup
DB_NAME = "rules.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL,
            ast_json TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Node class for AST representation
class Node:
    def __init__(self, type: str, left: Optional['Node'] = None, right: Optional['Node'] = None, value: Optional[Any] = None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }

# Helper function to convert rule string to AST
def create_ast(rule_string: str) -> Node:
    # This is a basic placeholder implementation.
    # In production, you would parse the string properly.
    if "AND" in rule_string:
        left, right = rule_string.split("AND", 1)
        return Node("operator", create_ast(left.strip()), create_ast(right.strip()), "AND")
    elif "OR" in rule_string:
        left, right = rule_string.split("OR", 1)
        return Node("operator", create_ast(left.strip()), create_ast(right.strip()), "OR")
    else:
        return Node("operand", value=rule_string.strip())

# API endpoint to create a rule
class RuleRequest(BaseModel):
    rule_string: str

@app.post("/create_rule/")
def create_rule(request: RuleRequest):
    try:
        ast = create_ast(request.rule_string)
        ast_json = json.dumps(ast.to_dict())

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", (request.rule_string, ast_json))
        conn.commit()
        conn.close()

        return {"message": "Rule created successfully", "ast": ast.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to evaluate a rule
class EvaluateRequest(BaseModel):
    data: Dict[str, Any]

@app.post("/evaluate_rule/")
def evaluate_rule(request: EvaluateRequest):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT ast_json FROM rules ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="No rules found.")

    ast_json = json.loads(result[0])
    return {"result": evaluate_ast(ast_json, request.data)}

def evaluate_ast(node: Dict, data: Dict) -> bool:
    if node["type"] == "operator":
        left = evaluate_ast(node["left"], data)
        right = evaluate_ast(node["right"], data)
        if node["value"] == "AND":
            return left and right
        elif node["value"] == "OR":
            return left or right
    elif node["type"] == "operand":
        return eval(node["value"], {}, data)  # Use eval cautiously!

# Streamlit UI
def streamlit_ui():
    st.title("Rule Engine with AST")

    st.header("Create a Rule")
    rule_input = st.text_area("Enter rule string", value="age > 30 AND department == 'Sales'")
    if st.button("Create Rule"):
        response = create_rule(RuleRequest(rule_string=rule_input))
        st.success(response["message"])
        st.json(response["ast"])

    st.header("Evaluate a Rule")
    age = st.number_input("Age", min_value=0, max_value=120, value=35)
    department = st.text_input("Department", value="Sales")
    salary = st.number_input("Salary", min_value=0, value=60000)
    experience = st.number_input("Experience", min_value=0, max_value=50, value=3)

    if st.button("Evaluate"):
        data = {"age": age, "department": department, "salary": salary, "experience": experience}
        response = evaluate_rule(EvaluateRequest(data=data))
        st.write(f"Result: {'Eligible' if response['result'] else 'Not Eligible'}")

# Run both FastAPI and Streamlit
if __name__ == "__main__":
    import threading

    # Run FastAPI server in a separate thread
    def run_fastapi():
        uvicorn.run(app, host="0.0.0.0", port=8000)

    api_thread = threading.Thread(target=run_fastapi, daemon=True)
    api_thread.start()

    # Run Streamlit UI
    streamlit_ui()
