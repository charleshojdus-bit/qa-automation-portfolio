

# QA Automation Portfolio

This project demonstrates a Python-based QA automation framework using Selenium WebDriver and Pytest. It is designed to showcase clean test design, maintainability, and real-world UI testing scenarios.

---

## 🚀 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

---

## 🧠 Key Concepts Demonstrated

* Page Object Model (POM) for separation of test logic and UI interactions
* Explicit waits for test stability and reliability
* Reusable page components and clean method design
* End-to-end UI test scenarios

---

## 📂 Project Structure

```
qa-automation-portfolio/
├── pages/          # Page Object classes (how actions are performed)
├── tests/          # Test cases (what is being tested)
├── conftest.py     # Shared test setup (driver fixture)
├── requirements.txt
```

---

## 🧪 Test Coverage

* Login functionality (valid, invalid, empty fields, locked user)
* Inventory page validation
* Add item to cart
* Remove item from cart

---

## ⚙️ Setup & Run

Clone the repository:

```bash
git clone https://github.com/charleshojdus-bit/qa-automation-portfolio.git
cd qa-automation-portfolio
```

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest -v -s
```

---

## 🎯 Purpose

This project focuses on building a solid foundation in QA automation by emphasizing:

* readable and maintainable test code
* realistic user workflows
* stability over quick scripts

---

## 📌 Notes

This framework is actively being expanded with additional test scenarios and improvements in structure, stability, and scalability.



