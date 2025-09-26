# Automation QA Challenge
Automation scripts and manual testing documentation for the QA Automation challenge for a Music School Management System.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tests](#tests)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

## Project Structure
- `tests/` - Automated test scripts using Python + Selenium
  - `e2e/` - End-to-end test cases
  - `pages/` - Page Object Model scripts
- `data/` - Test data generators and cleanup utilities
- `helpers/` - Utility functions for waits and validations
- `reports/` - Test execution reports
- `.env` - Environment variables (not committed to GitHub)
- `requirements.txt` - Python dependencies
- `README.md` - Project overview

## Getting Started
1. Clone the repository
   ```bash
   git clone https://github.com/Hemanth9317/Automation_QA_Challenge.git
   cd Automation_QA_Challenge

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt


- **How to Run Tests**  
```markdown
## How to Run
Run all E2E tests using:
```bash
pytest tests/e2e/

Run a specific test file:
pytest tests/e2e/test_student_onboarding.py


- **Dependencies**  
```markdown
## Dependencies
- Python 3.10+
- Selenium
- PyTest
- Any other dependencies from requirements.txt

Notes / Contributing
## Contributing
- Please ensure you follow the existing folder structure
- Add new tests in `tests/e2e` or `tests/pages` accordingly
- Track empty folders using `.gitkeep`
