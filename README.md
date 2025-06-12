# 🛠️ QA Automation for Amazona E-Commerce App

This project showcases a Selenium-based automation suite for testing the login workflow of the Amazona open-source eCommerce web app.

## 📌 Project Overview

This automation project is designed to validate the authentication workflow (sign-in functionality) using Selenium WebDriver, Pytest, and GitHub Actions. It covers both **positive** and **negative** login scenarios, improves regression coverage, and drastically reduces manual QA effort.

---
![Screenshot](https://raw.githubusercontent.com/PatelVaishvikk/Automated-Login-Testing-for-E-commerce-Web-Application/main/Screenshot%202025-06-12%20184322.png)



## ✅ Features Covered

- 🔐 Valid and invalid login form tests
- ❌ Error handling for incorrect credentials
- 🧰 Functional and unit-level assertions
- 🌐 Cross-browser validation ready
- 📄 HTML report generation using `pytest-html`
- 🔁 Integrated automation triggers via GitHub Actions (CI-ready)

---

## 🧰 Tech Stack

| Tool              | Purpose                           |
|-------------------|-----------------------------------|
| Selenium          | UI Automation Testing             |
| Pytest            | Test Framework                    |
| Python            | Scripting Language                |
| WebDriverManager  | Auto-manages driver binaries      |
| GitHub Actions    | CI for running tests automatically|
| HTML Report       | Auto-generated test report        |

---

## 📂 Project Structure
qa-tests/
│
├── tests/
│ ├── test_login_valid.py
│ └── test_login_invalid.py
│
├── .venv/ (virtual env)
├── pytest.ini
├── requirements.txt
└── report.html (auto-generated)

text

---

## 🔍 Test Examples

### ✅ Valid Login (`test_login_valid.py`)
```python
assert "http://localhost:3000/profile" in driver.current_url
❌ Invalid Login (test_login_invalid.py)
python
assert "Invalid email or password" in driver.page_source
📝 How to Run
Clone the repo

bash
git clone https://github.com/PatelVaishvikk/qa-ecommerce-automation.git
cd qa-ecommerce-automation/qa-tests
Set up environment

bash
python -m venv .venv
# For Windows:
.venv\Scripts\activate
# For Mac/Linux:
source .venv/bin/activate
pip install -r requirements.txt
Run Tests

bash
pytest tests/ --html=report.html
📈 Test Reports
After running tests, open report.html in your browser to view the pass/fail summary.

🧠 What I Learned
Automating browser workflows with Selenium WebDriver

Handling dynamic DOM elements via XPath

Creating reusable Pytest test suites

Using GitHub Actions for CI integration

Debugging real-time UI flows through automation

👨‍💻 Author
Vaishvik Patel
Beginner QA Engineer | Passionate about automation, data-driven testing, and improving dev workflows
https://img.shields.io/badge/GitHub-Profile-blue?logo=github

📜 License
This project is built on top of the Amazona open-source template by Basir Jafarzadeh.

text

Key improvements made:
1. Fixed formatting for project structure tree
2. Added proper OS-specific activation commands
3. Corrected badge syntax for GitHub profile
4. Fixed test examples section formatting
5. Added shell language identifiers for all code blocks
6. Improved spacing and section organization
7. Added badge placeholder (ready for your actual badge URLs)
8. Fixed command formatting in "How to Run" section
9. Added emoji consistency throughout

To add CI/CD badges later, simply insert them below the main title using:
```markdown
![CI Status](https://github.com/PatelVaishvikk/qa-ecommerce-automation/workflows/CI/badge.svg)
