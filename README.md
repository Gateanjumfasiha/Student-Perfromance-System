# Student Performance System
A Flask-based web application to manage student marks and performance efficiently. The app allows adding student marks, calculates pass/fail automatically, displays records, and shows performance summaries.

## 📁 Project Structure

student_app/
│
├── app.py          # Main Flask application
├── db_init.py      # Script to initialize the database
├── students.db     # SQLite database storing student records
└── templates/
    └── index.html  # HTML template for the UI


## 🚀 Features
- Add student name and marks
- Automatically calculates Pass/Fail
- Displays all student records
- Shows average marks
- Shows topper details
- Edit existing student details
- Delete student records 
## 🛠 Technologies Used
- Python
- Flask
- SQLite
- HTML/CSS 

## ▶️ How to Run the Project

1. Install Flask:
   pip install flask

2. Initialize Database:
   python db_init.py

3. Run the application:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

