# Automated Event Planner and Approval System - Phase 1

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue.svg)
![Git](https://img.shields.io/badge/Git-Enabled-orange.svg)
![AI-Assisted](https://img.shields.io/badge/AI--Assisted-Development-green.svg)

## Executive Summary
The "Automated Event Planner and Approval System" aims to digitize institutional workflows at JNU Jaipur. By replacing traditional, paper-based event approval pipelines with a transparent, responsive digital platform, this system reduces delays, ensures accountability, and streamlines the event planning procedures (as detailed in Section 3.2 of the project synopsis).

## Phase 1 Scope: Initial System Setup
This repository contains the deliverables for **Phase 1: Initial System Setup**. It establishes the robust foundation needed for subsequent feature development, including:
- Modular Blueprint Architecture (`main` and `events` routes)
- Dynamic Template Inheritance using Jinja2
- Organized Static Assets management
- Initial Error Handling & Routing
- Cloud-Ready Configuration (Ready for migration from SQLite for Dev to PostgreSQL for Production)

## Tech Stack
- **Backend Environment**: Python 3.8+, Flask 2.x
- **Templating**: Jinja2
- **ORM & Database**: SQLAlchemy (SQLite dev -> PostgreSQL prod)
- **Frontend**: HTML5, CSS3, JavaScript
- **Production Server**: Gunicorn
- **Proxy/Routing Middleware**: Werkzeug (ProxyFix)

## Installation Guide (Local Development)

Step-by-step instructions to get the Phase 1 foundation running locally.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CyberSential22/epas-phase-1.git
   cd epas-phase-1
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory (do not commit this file):
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secure_development_key
   ```

5. **Run the Application Locally**:
   ```bash
   python run.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Project Structure

```text
epas-phase-1/
├── app/
│   ├── blueprints/    # Application modules (main, events, admin)
│   ├── models.py      # Database schema (SQLAlchemy)
│   ├── utils/         # Helpers (e.g., ip_utils for Audit Logging)
│   ├── templates/     # HTML Jinja2 templates
│   ├── static/        # CSS, JS, Images
│   ├── errors.py      # Global error handlers
│   ├── config.py      # Env-based configurations
│   └── __init__.py    # Application factory
├── instance/          # Holds local dev.db (ignored in git)
├── logs/              # Local application logs
├── .gitignore         # Excluded files and folders 
├── venv/              # Virtual Environment
├── run.py             # Entry point
├── vercel.json        # Vercel proxy configuration
└── requirements.txt   # Project dependencies
```

## Deployment Overview
As part of our continuous delivery setup (Section 16), the application architecture heavily utilizes cloud platforms:
- **Frontend Proxy**: [Vercel](https://vercel.com) handling ingress traffic and static acceleration.
- **Backend API**: [Render](https://render.com) serving the heavy-lifting Python/Flask logic via Gunicorn.
- **Database**: [Supabase](https://supabase.com) (Serverless PostgreSQL) ensuring scalable data integrity.

## Acknowledgments
- **Project Team**: Kashif Shaikh, Aditya Gond, Yaduvansh Singh Ranawat (CyberSential22)
- **Project Guide**: Ms. Saumya, JNU Jaipur
- **AI-Assisted Development**: Developed with adherence to Section 6.5 of the guidelines indicating ethical use of AI-assisted tools for rapid architectural setup, design suggestions, and research, while preserving student ownership and core system orchestration.

## License
Provided under the [MIT License](LICENSE).
