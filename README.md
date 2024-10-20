# Zeotap-SE-Intern-Assignment

This Repository contains all my assignments for Zeotap Software Engineer Intern.


# **1) Rule Engine with AST**

This project is a **3-tier rule engine application** with a **Simple UI (Streamlit)**, **API (FastAPI)**, and **Backend (SQLite Database)**. The system uses an **Abstract Syntax Tree (AST)** to represent dynamic rules and evaluates user eligibility based on attributes like age, department, salary, and experience.

---

## **Table of Contents**
1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [API Endpoints](#api-endpoints)  
6. [Sample Inputs](#sample-inputs)  
7. [Bonus Features](#bonus-features)  
8. [Project Structure](#project-structure)  
9. [How to Run](#how-to-run)  
10. [License](#license)

---

## **Features**
- Create, modify, and combine rules using AST.  
- Evaluate rules dynamically based on user data.  
- Uses **FastAPI** for backend and **Streamlit** for UI.  
- Stores rules and metadata in **SQLite** database.  
- Validates inputs and handles rule errors gracefully.

---

## **Tech Stack**
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** SQLite  
- **Language:** Python 3.x  

---

## **Installation**

### **Prerequisites**
- Python 3.x installed on your machine  
- Git installed

### **Steps**
1. **Clone the Repository**
   ```bash
   git clone <your-github-repo-url>
   cd <your-repo-directory>
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database**
   The application will create an SQLite database (`rules.db`) automatically during the first run.

---

## **Usage**

### **Run the Application**
```bash
python main.py
```

- **FastAPI Backend**: Runs on `http://localhost:8000`  
- **Streamlit UI**: Accessible at `http://localhost:8501`

---

## **API Endpoints**
1. **Create Rule**  
   **POST** `/create_rule/`  
   **Request Body:**
   ```json
   {
     "rule_string": "(age > 30 AND department == 'Sales')"
   }
   ```
   **Response:**  
   ```json
   {
     "message": "Rule created successfully",
     "ast": { ... }
   }
   ```

2. **Evaluate Rule**  
   **POST** `/evaluate_rule/`  
   **Request Body:**
   ```json
   {
     "data": {
       "age": 35,
       "department": "Sales",
       "salary": 60000,
       "experience": 3
     }
   }
   ```
   **Response:**  
   ```json
   {
     "result": true
   }
   ```

---

## **Sample Inputs**

### **Sample Rule String:**
```plaintext
((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
```

### **Sample Data for Evaluation:**
```json
{
  "age": 35,
  "department": "Sales",
  "salary": 60000,
  "experience": 3
}
```

**Expected Output:**  
`True`

---

## **Bonus Features**
- **Validation and Error Handling:** Handles invalid rules or malformed data gracefully.
- **Cross-Origin Resource Sharing (CORS):** Enabled to allow access from different origins.
- **Threaded Backend and Frontend:** FastAPI and Streamlit run concurrently for seamless operation.

---

## **Project Structure**
```
/project-root
│
├── main.py               # Combined code for FastAPI and Streamlit
├── requirements.txt      # Dependencies
├── rules.db              # SQLite database (auto-created on first run)
└── README.md             # Documentation (this file)
```

---

## **How to Run**

1. **Start the Application**
   ```bash
   python main.py
   ```

2. **Access the UI**
   - Open your browser and go to: `http://localhost:8501`
   
3. **Test the API**
   - Use `curl` or Postman to test the `/create_rule/` and `/evaluate_rule/` endpoints.

---

## **License**
This project is licensed under the MIT License. Feel free to modify and distribute.

---

## **Contributors**
- [Gopinath.R](https://github.com/Gopinath14141)
