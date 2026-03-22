# Automated Event Planner and Approval System - Phase 1

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue?logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?logo=git&logoColor=white)
![AI-Assisted](https://img.shields.io/badge/AI--Assisted-Development-brightgreen)

## Executive Summary
The "Automated Event Planner and Approval System" is designed to digitize institutional workflows at JNU Jaipur. By replacing legacy paper-based approvals with a secure, transparent, and efficient digital platform, this system streamlines event planning, request submissions, and administrative approvals, significantly reducing administrative overhead and increasing transparency across the university.

## Phase 1 Scope
This repository encompasses the **Phase 1: Initial System Setup**. It lays the foundational architecture required for future development and deployment. The scope includes:
- A modular Blueprint architecture (`admin`, `auth`, `main`, etc.).
- Robust Jinja2 template inheritance for rapid UI development.
- Integration of static assets (CSS, JS) mapped to routes.
- Foundational routing and views.
- Preparation for cloud deployment, including a database schema ready for migration from local SQLite (development) to PostgreSQL (production).

## Tech Stack
- **Backend**: Python 3.8+, Flask 2.x, SQLAlchemy (ORM)
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2
- **Database**: SQLite (Dev) / PostgreSQL (Prod via Supabase)
- **Server**: Gunicorn

## Installation Guide

Follow these steps to set up the system locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/CyberSential22/epas-phase-1.git
   cd epas-phase-1
   ```

2. **Set up a Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-super-secret-key-change-me
   ```

5. **Run the Application**
   ```bash
   flask run
   # Or using the run script directly:
   python run.py
   ```

## Project Structure
```text
epas-phase-1/
├── app/
│   ├── __init__.py       # Application factory
│   ├── config.py         # Configuration classes
│   ├── models/           # Database models
│   ├── utils/            # Helper utilities and IP logging
│   ├── routes/           # Blueprint route definitions
│   ├── templates/        # Jinja2 HTML templates
│   └── static/           # CSS, JS, and Images
├── instance/             # Local SQLite databases (Auto-generated, untracked)
├── run.py                # Application entry point
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel proxy configuration
├── .gitignore            # Ignored files configuration
└── README.md             # Project documentation
```

## Deployment Overview
This project is structured for a modern, decoupled cloud deployment strategy:
- **Frontend Proxy (Vercel)**: Acts as a reverse proxy, handling edge caching and continuous deployment.
- **Backend Hosting (Render)**: Hosts the Python Flask application using Gunicorn.
- **Database (Supabase)**: Offers a managed PostgreSQL database instance tailored for production.

## Acknowledgments
This project is developed by **Kashif Shaikh, Aditya Gond, and Yaduvansh Singh Ranawat** under the guidance of **Ms. Saumya** at JNU Jaipur. 
*Note on AI Usage (Section 6.5): AI-assisted tools were utilized ethically for research, debugging, and code generation, while the student team maintained full ownership and understanding of the core system design, logic, and architecture.*

## License
This project is licensed under the MIT License.
