# Generic Python UI Automation Framework

This repository hosts a basic, yet extensible, UI automation framework built with Python and Selenium WebDriver. It demonstrates how to implement fundamental concepts like the Page Object Model (POM) and a Driver Factory for creating robust and scalable web UI tests.

The framework is designed to be a starting point for developing automated tests for web applications, focusing on clean code, maintainability, and best practices.

## Features

* **Selenium WebDriver:** Utilizes Selenium for browser automation and interaction.
* **Page Object Model (POM):** Implements the POM design pattern for better test readability, reusability, and maintainability by separating UI elements and interactions from test logic.
* **Driver Factory Pattern:** Centralizes WebDriver initialization and configuration, allowing for flexible browser selection (e.g., Chrome, Firefox) and running tests in different modes (e.g., headless).
* **`unittest` Framework:** Uses Python's built-in `unittest` module for test case organization and execution.
* **Base Test Fixture:** Provides common setup and teardown logic for all test cases, including WebDriver management.
* **Example Google Search Test:** Includes a sample test case demonstrating how to automate a Google search.

## Project Structure

```

├── fixtures/
│   └── base_test_fixture.py
├── pages/
│   ├── base_page_object.py
│   └── google_home_page.py
├── tests/
│   └── test_web_driver.py
└── utils/
    └── driver_factory.py

````

* **`base_page_object.py`**:
    Defines the `BasePage` class, which serves as the base for all Page Objects. It typically holds common WebDriver functionalities applicable across different web pages.
* **`driver_factory.py`**:
    Implements the Driver Factory pattern. This module is responsible for creating and configuring different WebDriver instances (e.g., Chrome, Firefox) with various options (like headless mode).
* **`base_test_fixture.py`**:
    Extends `unittest.TestCase` and provides a base class for all test cases. It manages the lifecycle of the WebDriver, using the `DriverFactory` for initialization and handling browser cleanup (close and quit).
* **`google_home_page.py`**:
    An example Page Object for the Google search home page. It encapsulates elements (like the search input and button) and actions (like performing a search) related to that page.
* **`test_home_page.py`**:
    A sample test case demonstrating how to use the framework to automate a simple Google search. It inherits from `BaseTestFixture`.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x installed on your system.
* `pip` (Python package installer).
* Google Chrome browser installed.
* ChromeDriver executable compatible with your Chrome browser version. (It's recommended to place `chromedriver` in a location accessible by your system's PATH, or to use a library like `webdriver-manager` to handle this automatically).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/harbourc/Generic_Python_UI_Auto.git
    cd Generic_Python_UI_Auto
    ```

2.  **Install dependencies:**
    It's recommended to create a virtual environment first:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    Then, install the required Python packages:
    ```bash
    pip install selenium
    ```
    *(Optional but recommended: `pip install webdriver-manager` if you want to automatically manage ChromeDriver versions)*

## How to Run Tests

You can run the tests directly from the command line using Python's `unittest` module.

1.  **Ensure your `chromedriver` is correctly set up.**
2.  **Navigate to the project root directory** in your terminal.
3.  **Run the test file:**
    ```
    python test_web_driver.py
    ```
    This will execute the `test_should_search_google` test case, open a Chrome browser, perform the search, and close the browser.

## Future Enhancements & Scaling (Roadmap)

This framework is designed to be expandable. Here are some potential areas for future development to scale it for large-scale enterprise applications:

* **Configuration Management:** Externalize test data and environment-specific settings (URLs, credentials, browser types) into configuration files (e.g., `.ini`, YAML, JSON) for easier management.
* **Advanced Reporting:** Integrate with powerful reporting tools like Allure Reports or `pytest-html` to generate rich, interactive test execution reports with screenshots on failure.
* **Parallel Execution:** Implement parallel test execution using tools like `pytest-xdist` or by leveraging Selenium Grid/cloud-based Selenium services (BrowserStack, Sauce Labs, LambdaTest).
* **CI/CD Integration:** Containerize the test environment using Docker and integrate test execution into Continuous Integration/Continuous Delivery pipelines (e.g., Jenkins, GitHub Actions, GitLab CI).
* **Comprehensive Logging:** Implement detailed logging throughout the framework for better debugging and traceability.
* **Error Handling & Retries:** Add more robust error handling mechanisms and automatic retry logic for flaky tests.
* **Cross-Browser Testing:** Extend the `DriverFactory` to easily support and run tests across multiple browsers (Firefox, Edge, Safari, etc.).
