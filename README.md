# Automated Event Planner and Approval System - Phase 1

Welcome to Phase 1 of the Automated Event Planner and Approval System! This project aims to digitize and manage the end-to-end lifecycle of event planning and subsequent approvals.

## 🚀 Phase 1 Goals and Implementation
Phase 1 focuses on setting up the fundamental architecture and scaffolding for the application.

### Features
- **Project Structure**: Initialized a structured, scalable Flask architecture (Model-View-Controller pattern).
- **Core Models**: Created robust SQLAlchemy models defining `User` and `Event` (handling creation, pending, approved, and rejected states).
- **Configuration & Setup**: Set up simple and robust development configuration tools including `.env` and `config.py`.
- **Server Startup Scripts**: Included `run_server.bat`, `quick_server.bat`, and `setup.sh` to get up and running smoothly across different platforms.

## 📁 Project Layout
```
/
├── app/                  # Main application package
│   ├── blueprints/       # Flask blueprints for organizing sub-applications
│   ├── routes/           # Request handlers and routing logic
│   ├── static/           # Static assets (CSS, JS, Images)
│   ├── templates/        # HTML templates for rendering views
│   ├── utils/            # Helper scripts and utilities
│   ├── config.py         # App logic configurations
│   ├── errors.py         # Custom application error handlers
│   ├── models.py         # SQLAlchemy database models
│   └── __init__.py       # Application factory
├── instance/             # Local system configurations and SQLite database
├── venv/                 # Virtual Python interpreter environment
├── .env                  # Environment variables
├── config.py             # Global system configurations
├── requirements.txt      # Python dependencies
├── run.py                # Main application entry point
└── setup.sh / *.bat      # Platform-specific initialization scripts
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Quick Start (Windows)
1. Double click `quick_server.bat` to automatically set up the virtual environment, install dependencies, and run the server.

*Alternatively manually:*
1. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```cmd
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
4. Run the application:
   ```cmd
   python run.py
   ```
   (Or simply use `run_server.bat`)

### Quick Start (Unix/Linux/Mac)
1. Run the setup shell script:
   ```bash
   bash setup.sh
   ```
2. Run the application manually if needed:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   python run.py
   ```

## 📜 Next Steps (Phase 2)
The next phase will likely introduce full user authentication, role-based access control (RBAC), and user interface development using the established templates.
