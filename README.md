# 🚀 Employee Onboarding Automation System

An HR Tech automation system that streamlines employee onboarding by automatically creating onboarding tasks, assigning training resources, sending welcome emails, and scheduling probation reminders.

This project demonstrates how **HR expertise, workflow automation, and AI-ready architecture** can be combined to improve operational efficiency while maintaining a human-centered employee experience.

---

## 🌟 Overview

Employee onboarding is often repetitive, manual, and prone to inconsistency—especially for growing teams and small organizations. This system automates core onboarding activities to ensure every new hire receives a structured, timely, and welcoming onboarding experience.

The automation handles:
- Task creation for onboarding checklists
- Assignment of training and resources
- Welcome communication
- Reminder scheduling for probation reviews

The goal is to **reduce administrative workload** for HR teams while creating a **consistent and positive first experience** for new employees.

---

## 📂 Project Structure

```text
employee-onboarding-automation/
│
├─ src/
│  ├─ main.py
│  ├─ clickup_client.py
│  ├─ gmail_client.py
│  ├─ templates.py
│  └─ utils.py
│
├─ data/
│  ├─ email_templates.json
│  ├─ new_hire.sample.json
│  ├─ onboarding_checklist.json
│  └─ welcome_email_template.txt
│
├─ results/
│  └─ .gitkeep
│
├─ .env.example
├─ requirements.txt
├─ case-study.md
└─ README.md

```

## 🚀 Features

### ✔ Automated Onboarding Task Creation  
Creates ClickUp tasks from a standardized onboarding checklist for each new hire.

### ✔ Training & Resource Assignment  
Automatically assigns training tasks and learning materials based on role or department.

### ✔ Welcome Email Automation  
Generates and sends personalized welcome emails to new employees (via Gmail API).

### ✔ Probation & Check-In Reminders  
Schedules follow-up tasks and reminders for probation reviews and check-ins.

### ✔ Modular & Extendable Design  
Built with scalability in mind—can integrate with additional HR tools and systems.

---

## 🧠 How It Works

### 1. New Hire Data Input  
HR provides new hire details in a structured JSON file (name, role, start date, manager, etc.).

### 2. Task Automation  
The system reads a predefined onboarding checklist and creates corresponding ClickUp tasks.

### 3. Communication & Scheduling  
Welcome emails are generated and sent, and reminder tasks are scheduled for key milestones.

### 4. Execution Logging  
Each automation run is logged for transparency, auditing, and troubleshooting.

📥 Input Example (new_hire.json)

```json

{
  "full_name": "James Walker",
  "email": "james.walker@email.com",
  "role": "IT Support Officer",
  "start_date": "2026-01-05",
  "manager_name": "Sarah Lee",
  "department": "IT"
}

```

---


## 🛠 Tech Stack

- **Python**
- **ClickUp API**
- **Gmail API**
- **python-dotenv**
- **JSON-based configuration**
- **VS Code & GitHub**

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/employee-onboarding-automation.git
cd employee-onboarding-automation

```


### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. Configure environment variables

Create a .env file using .env.example and add your credentials:

```env

CLICKUP_API_TOKEN=your_clickup_token
CLICKUP_LIST_ID=your_clickup_list_id

```

### 4. Add new hire data

Create or update a JSON file in the data/ folder with the new hire’s details.

### 5. Run the automation

```bash
python src/main.py --new-hire data/new_hire.json


```

Once executed, onboarding tasks will be created in ClickUp and execution logs will be saved in the results/ folder.


---

## 🖼 Demo or Live Project

This project runs locally using authenticated API connections.  
Sample outputs and execution logs are stored in the `results/` folder.

Screenshots and demo walkthroughs can be added to the `assets/` folder for documentation and portfolio presentation.

---

## 🗺 Roadmap

### Phase 1 — MVP (Current)
- ClickUp onboarding task automation  
- Structured new hire input  
- Execution logging  

### Phase 2 — Communication Enhancements
- Gmail API integration  
- Email templates  
- Calendar event creation  

### Phase 3 — Advanced HR Workflows
- Role-based onboarding flows  
- Probation evaluation automation  
- HR dashboard integration  

### Phase 4 — Integrations & Scaling
- Integration with ATS systems  
- Notion or HRIS sync  
- Multi-team onboarding pipelines  

---

## 🎯 What I Learned

Building this system reinforced key lessons in HR-Tech automation:

- ✔ Translating HR processes into executable workflows  
- ✔ Designing scalable and modular automation systems  
- ✔ Managing external APIs securely and responsibly  
- ✔ Balancing efficiency with a human-centered employee experience  
- ✔ Applying automation to solve real operational HR challenges  

---

## 🌍 Long-Term Vision

This project serves as a foundation for a broader **HR operations automation platform** that supports:

- Seamless employee lifecycle management  
- Consistent onboarding experiences  
- Reduced administrative overhead  
- Scalable HR workflows for growing organizations  

The ultimate goal is to **empower HR teams through automation**, allowing them to focus on people—not paperwork.

---


## 📬 Contact
👩‍💻 Created by: **Charlote Araneta**

🔗 LinkedIn: https://www.linkedin.com/in/charlotearaneta

🌐 Portfolio: https://charlotearaneta.github.io

---
