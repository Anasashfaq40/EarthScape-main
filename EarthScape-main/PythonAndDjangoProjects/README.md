## Instructions
1. Download zip file and extract it
2. To set up the project, you can use the following commands:
```

Here’s how you can structure your **README.txt** file (without code) to ensure your project runs successfully and includes clear instructions for setup and usage:

---

## **Real-Time Monitoring and Feedback Dashboard**

This document provides step-by-step instructions to set up and run the **Real-Time Monitoring and Feedback Dashboard**, which integrates Django as a backend and Streamlit as a frontend for real-time data monitoring and user feedback.

---

### **1. Overview**

The project offers real-time monitoring of metrics (like temperature and humidity) and a feedback system for user input. Users can:
- Set thresholds for alerts.
- Start and stop real-time monitoring.
- Provide feedback or report issues.

**Core Features**:
1. Real-time data visualization.
2. Configurable threshold-based alerts.
3. Feedback and support form for user interaction.

---

### **2. Prerequisites**

Before running the project, ensure the following:
- Python 3.9 or higher is installed.
- A virtual environment tool like `venv` or `virtualenv` is recommended.
- Internet access to install dependencies.

---

### **3. Project Structure**

The project is divided into two main components:

1. **Backend (Django)**:
   - Manages APIs, database interactions, and business logic.
   - Provides endpoints for real-time data and feedback handling.

2. **Frontend (Streamlit)**:
   - Displays real-time charts and interactive user inputs.
   - Provides a feedback submission form.

---

### **4. Installation Instructions**

#### **Step 1: Clone the Project**
Download the project files to your system.
```bash
git clone <repository_url>
cd project_directory
```

#### **Step 2: Install Dependencies**
Create a virtual environment (optional but recommended) and install the required packages.

For a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### **5. Running the Backend**

1. Navigate to the backend folder:
   ```bash
   cd backend/
   ```

2. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

3. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. Access the backend at:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### **6. Running the Frontend**

1. Navigate to the frontend folder:
   ```bash
   cd frontend/
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Access the frontend at the URL displayed in the terminal (e.g., [http://localhost:8501](http://localhost:8501)).

---

### **7. Features Guide**

#### **Real-Time Monitoring**
- Click **"Start Monitoring"** to begin real-time data visualization.
- Click **"Stop Monitoring"** to pause updates and analyze the current state.
- Adjust temperature and humidity thresholds using the sliders to set alert conditions.

#### **Feedback and Support**
- Fill in your **name**, **email**, and detailed feedback or issue in the provided form.
- Click **"Submit Feedback"** to send your input for review.

---

### **8. Troubleshooting**

1. **Django Server Not Running**:
   - Ensure all migrations are applied using:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Restart the server with:
     ```bash
     python manage.py runserver
     ```

2. **Streamlit App Not Opening**:
   - Ensure Streamlit is installed by running:
     ```bash
     pip install streamlit
     ```
   - Start the app again using:
     ```bash
     streamlit run main.py
     ```

3. **Dependency Issues**:
   - Ensure all dependencies are installed using:
     ```bash
     pip install -r requirements.txt
     ```

4. **Database Issues**:
   - If the database is not set up, delete `db.sqlite3` in the backend folder and reapply migrations.

---

### **9. Future Improvements**

This project can be extended to:
1. Add email notifications for threshold alerts.
2. Implement authentication for feedback submission.
3. Upgrade from SQLite to a more robust database like PostgreSQL for scalability.
4. Deploy the system to cloud platforms like AWS or Heroku for production use.

---


<!-- Running Python Scripts: -->
<!-- data-science-EarthScape (clean & sort) Folder -->
python sort.py
python index.py

Sure, here is your one line in English:

<!---------Model Training----------!>
<!-- Model Training -->
You need to download and install Anaconda to use this for model training. 
model training.ipynb
<!-- using jupyter -->
<!-- download link -->
https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Windows-x86_64.exe
```

## 🔗 Important Links
- [Figma ProtoType](https://www.figma.com/design/7N179nlDReqDi837C6edPh/EarthScape?node-id=0-1&t=NeZGGVjHXZU62090-1)
- [Tableau Data Visualization](https://public.tableau.com/app/profile/muhammad.taha2039/viz/EarthScape/TrendoverTime)


## Team Behind ViroShield

| Student Id | Student Name |
| ------------- | ------------- |
| Student1415086 | Muhammad Anas  |
| Student1414152 | Muhammad Taha |
| Student1448007 | Bharti Gurnani |
| Student1406511 | Anum Asghar |

