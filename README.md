# 🛒 E-Commerce Website Testing Automation

This project automates testing of the SauceDemo e-commerce website using Selenium with Python and Pytest framework.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)
![Status](https://img.shields.io/badge/Tests-Passing-brightgreen)
---

# 📌 Project Overview

The main objective of this project is to perform:

- Manual Testing
- Automation Testing
- Functional Testing
- UI Testing

on the SauceDemo application.

Website Used:
https://www.saucedemo.com/

---

# 🚀 Features Automated

✅ Login Functionality  
✅ Add Product to Cart  
✅ Checkout Process  
✅ Logout Functionality  
✅ Screenshot Capture  
✅ HTML Report Generation  

---

# 🛠 Technologies Used

<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40"/> <b>Python</b>  
<br><br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="40" height="40"/> <b>Selenium WebDriver</b>  
<br><br>

<img src="https://pytest.org/en/latest/_static/pytest_logo_curves.svg" width="90"/> <b>Pytest Framework</b>  
<br><br>

<img src="https://raw.githubusercontent.com/pytest-dev/pytest-html/master/docs/_static/pytest-html-logo.png" width="120"/> <b>Pytest HTML Report</b>  
<br><br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="40" height="40"/> <b>Visual Studio Code (VS Code)</b>  
<br><br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/chrome/chrome-original.svg" width="40" height="40"/> <b>Google Chrome Browser</b>

</p>

---

# 📂 Project Structure

```bash
Ecommerce_Testing_Project/
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── pages/
│   ├── login_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── logout_page.py
│
├── screenshots/
├── reports/
├── manual_testing/
│
├── README.md
├── pytest.ini
└── requirements.txt
```

---

# ▶️ How to Run Project

## Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2 — Run Tests

```bash
python -m pytest
```

---

## Step 3 — Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# 📸 Project Screenshots

Screenshots are automatically saved inside the screenshots folder after successful test execution.

## Login Test

![Login Screenshot](screenshots/login.png)

---

## Cart Test

![Cart Screenshot](screenshots/cart_test.png)

---

## Checkout Test

![Checkout Screenshot](screenshots/checkout.png)

---

## Logout Test

![Logout Screenshot](screenshots/logout.png)

---

# 📊 HTML Reports

HTML reports are generated inside the reports folder.



![HTML Report](screenshots/report.png)


---

# 🧪 Test Scenarios Covered

| Module | Scenario |
|---|---|
| Login | Valid & Invalid Login |
| Cart | Add Product to Cart |
| Checkout | Complete Product Checkout |
| Logout | Logout Functionality |

---

# 📁 Manual Testing Documents

The project also contains:

- Test Cases
- Bug Reports
- RTM
- Test Plan

inside the manual_testing folder.

---

# 👨‍💻 Author

Prajwal Chaudhari

GitHub:
https://github.com/prajwalchaudhari60

---

# ⭐ Future Enhancements

- Data Driven Testing
- Jenkins Integration
- Logging
- Cross Browser Testing
- Headless Browser Execution
