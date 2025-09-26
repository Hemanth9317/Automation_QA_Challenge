# Automation QA Challenge

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Pytest](https://img.shields.io/badge/tests-pytest-brightgreen)

Automation scripts and manual testing documentation for the QA Automation challenge for a Music School Management System (Student Onboarding Flow).

---

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tests](#tests)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

---

## Project Structure
Automation_QA_Challenge/
├── tests/
│ ├── e2e/ # End-to-end test cases
│ └── pages/ # Page Object Model scripts
├── data/ # Test data generators and cleanup utilities
├── helpers/ # Utility functions for waits and validations
├── reports/ # Test execution reports
├── .env # Environment variables (not committed)
├── requirements.txt # Python dependencies
├── README.md # Project overview
└── .gitignore # Ignored files/folders


---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Hemanth9317/Automation_QA_Challenge.git
cd Automation_QA_Challenge

Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

Install dependencies:
pip install -r requirements.txt

Add your .env credentials:
MMS_EMAIL=your-trial-email@example.com
MMS_PASSWORD=your-trial-password
MMS_SCHOOL_URL=https://your-school.mymusicstaff.com

Tests:
Run all E2E tests:
pytest tests/e2e/

Reports:
After running tests, generated reports can be saved in the reports/ folder.

Dependencies:
- Python 3.10+
- Selenium
- PyTest
- Other dependencies listed in requirements.txt

Contributing:
- Follow the existing folder structure when adding new scripts.

- Track empty folders using .gitkeep.

- Ensure your code is properly commented and adheres to Python best practices.

- Update README.md if new scripts or features are added.



















