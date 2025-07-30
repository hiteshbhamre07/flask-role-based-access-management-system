# Flask Role-Based Access Management System


This is a Flask web application that demonstrates **Role-Based Access Control (RBAC)** using Flask Blueprints. It allows user registration, login, and role-based access to specific routes and dashboards.

---

## 🚀 Features

- 🔒 User Authentication (Register / Login / Logout)
- 🧑‍⚖️ Role-Based Access (Admin, User, etc.)
- 📦 Modular Flask Blueprints
- 📊 Dashboard protected by role
- 🔐 Secure password hashing (with Werkzeug)
- ✅ Flash messages and form validations

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- MYSQL (or your DB of choice)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/hiteshbhamre07/flask-role-based-access-management-system.git
cd flask-role-based-access-management-system


###2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4.Run the App
python app.py

**🗂️ Project Structure**

flask-role-based-access-management-system/
│
├── app.py                     # Entry point
├── config.py                  # Configuration file
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── css/, js/, images/
│
├── auth/                      # 🔐 Auth Blueprint
│   ├── __init__.py
│   ├── routes.py
│   └── forms.py
│
├── admin/                     # 🧑 Admin Blueprint
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│
├── user/                      # 👤 User Blueprint
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│
└── models/                    # 📦 Models for User & Roles
    ├── __init__.py
    └── user_model.py


👤 Author
Hitesh Bhamre


You can save this in your repo by doing:

```bash
echo "[Paste above markdown]" > README.md
git add README.md
git commit -m "Add README"
git push

