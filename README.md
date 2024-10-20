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
   git clone https://github.com/Gopinath14141/Zeotap-SE-Intern-Assignment.git
   cd Zeotap-SE-Intern-Assignment
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
This project is licensed under the MIT License.

---

## **Contributors**
- [Gopinath.R](https://github.com/Gopinath14141)



# 2) ⛅ Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Description
This **Real-Time Data Processing System for Weather Monitoring** is a Streamlit-based application that fetches real-time weather data from the OpenWeatherMap API. The system offers insights into weather conditions across major Indian cities with aggregated daily summaries, alerts, and interactive visualizations. Users can monitor temperature trends, identify dominant weather conditions, and receive alerts based on configurable thresholds.

## Features
- **Continuous Weather Monitoring**: Retrieve real-time weather data for cities such as Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- **Daily Weather Summaries**: Aggregate data with metrics like:
  - Average, Maximum, and Minimum Temperatures
  - Dominant Weather Condition of the Day
- **Customizable Alerts**: Trigger alerts if temperatures exceed 35°C or based on other configured thresholds.
- **Visual Dashboard**: Interactive charts showcasing temperature trends and weather conditions.
- **User Preferences**: Choose cities to monitor and set temperature thresholds.

## Technologies Used
- **Python**  
- **Streamlit**: For building the interactive web interface  
- **Plotly**: For visualizing weather trends and conditions  
- **Pandas**: For data processing and aggregation  
- **Requests**: To call the OpenWeatherMap API

## **Project Structure**
```
/project-root
│
├── main.py               # Combined code for FastAPI and Streamlit
├── requirements.txt      # Dependencies
└── README.md             # Documentation (this file)
```


## Setup Instructions

### Prerequisites
- Python 3.x  
- OpenWeatherMap API key (Sign up [here](https://openweathermap.org/api) for a free key)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Gopinath14141/Zeotap-SE-Intern-Assignment.git
   cd Zeotap-SE-Intern-Assignment
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit plotly pandas requests
   ```

3. **Configure the API Key**:
   Open the `app.py` file and replace `API_KEY` with your actual API key:
   ```python
   API_KEY = "**********"
   ```

### Running the Application
To run the application locally, execute the following command:
```bash
streamlit run app.py
```
The Streamlit dashboard will open automatically in your default browser. Alternatively, you can visit `http://localhost:8501` to access the application.

## Usage
1. **Select Cities**: Use the sidebar to select the cities you want to monitor.
2. **Start Monitoring**: Click the "Start Monitoring" button to begin fetching weather data every 5 minutes.
3. **View Insights**:  
   - Observe current weather data and temperature trends.
   - Check the bar chart to see the most frequent weather conditions.
   - Monitor alerts for high temperatures.

## Visualizations
- **Line Chart**: Displays daily temperature trends (Average, Max, Min temperatures).
- **Bar Chart**: Visualizes the dominant weather conditions across selected cities.

## Bonus Features (Optional)
- **Additional Weather Metrics**: Supports future integration for wind speed, humidity, etc.
- **Forecasting Capabilities**: Extend to retrieve weather forecasts and generate predictions.

## Acknowledgements
- **OpenWeatherMap** for the weather data API.
- **Streamlit** for the easy-to-use web framework.
- **Plotly** for creating stunning visualizations.

## License
This project is licensed under the MIT License. 

## Contributors
[Gopinath.R](https://github.com/Gopinath14141)
