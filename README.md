# QA Automation Portfolio

This project demonstrates a Python-based QA automation framework using Selenium WebDriver and Pytest. It is designed to showcase clean test design, maintainability, and real-world UI testing scenarios.

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* Git / GitHub

---

## Key Concepts Demonstrated

* Page Object Model (POM) for separation of test logic and UI interactions
* Explicit waits for test stability and reliability
* Reusable page components and clean method design
* End-to-end UI test scenarios
* Regression testing through a full Pytest suite
* Debugging and stabilizing form interactions in a React-based UI

---

## Project Structure

```text
qa-automation-portfolio/
├── pages/              # Page Object classes (how actions are performed)
├── tests/              # Test cases (what is being tested)
├── conftest.py         # Shared test setup (driver fixture)
├── requirements.txt    # Project dependencies
└── README.md
```

---

## Test Coverage

The suite currently includes 12 passing tests covering:

* Login functionality

  * valid login
  * invalid password
  * empty fields
  * missing password
  * locked-out user
  * invalid username
* Inventory page validation
* Adding an item to the cart
* Cart badge verification
* Opening the cart
* Removing an item from the cart
* Full checkout flow

  * login
  * add item to cart
  * open cart
  * begin checkout
  * enter checkout information
  * complete order
  * verify confirmation message

---

## Recent Milestone

A full end-to-end checkout flow test was added and stabilized.

During development, the checkout form presented a validation issue where the input fields appeared to contain values, but the application still returned a required-field error. The issue was resolved by improving the checkout page object with a more reliable field-entry helper that updates the input value and dispatches input/change events.

The final checkout flow was verified with repeated test runs and the full test suite.

Current status:

```text
12 passed
```

---

## Setup and Run

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

Run the full test suite:

```bash
python -m pytest -v
```

Run the checkout test only:

```bash
python -m pytest tests/test_checkout.py -v
```

---

## Purpose

This project focuses on building a solid foundation in QA automation by emphasizing:

* readable and maintainable test code
* realistic user workflows
* stable browser interactions
* clear separation between tests and page behavior
* debugging based on evidence instead of guessing

---

## Next Improvements

Planned improvements include:

* GitHub Actions CI pipeline
* screenshots on test failure
* additional checkout validation tests
* improved reporting/test artifacts
* expanded API testing coverage in a future portfolio layer




