# Daily Focus and Energy Planner

**web-based productivity planner** built with **Flask and Docker**, featuring a To-Do list, energy-based task prioritization, and a dynamic focus-break plan with productivity scoring.

---

## Features

- **To-Do List** with full CRUD (Add, Edit, Delete) and task status tracking
- **Energy-based prioritization** (High, Medium, Low)
- **Focus & Break Plan** generated dynamically based on active tasks and energy levels
- **Productivity Score** calculated from focused work time
- **Dark/Light Theme UI**
- Fully **Dockerized** for consistent deployment across environments

## Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript  
- **Containerization:** Docker  

## Project Structure

daily-focus-planner/
│
├── app.py 
├── requirements.txt 
├── Dockerfile 
├── static/
│ ├── style.css 
│ └── script.js 
├── templates/
│ └── index.html 
└── README.md 

## Docker Setup

**1. Build Docker Image**

docker build -t daily-focus-planner .
2. Run Docker Container

docker run -p 5000:5000 daily-focus-planner
3. Open in Browser

http://localhost:5000

Flow:
Code backend & frontend → Create Dockerfile → Build image → Run container → Open in browser

How It Works
Add tasks to the To-Do list and assign an energy level (High / Medium / Low)

Update task status (Pending, In Progress, Completed)

Click Generate Focus Plan to dynamically calculate focus and break blocks based on active tasks

View productivity score and follow the schedule

Benefits
Demonstrates containerized application workflows

Practical task-driven focus management

Fully DevOps-ready and portable

Screenshots
<img width="1919" height="935" alt="Screenshot 2026-01-26 133019" src="https://github.com/user-attachments/assets/c9e46945-17e4-4f36-b411-61ebd6472113" />

<img width="1896" height="924" alt="Screenshot 2026-01-26 133033" src="https://github.com/user-attachments/assets/f8688ad7-0190-441a-ad64-11433b602e93" />


