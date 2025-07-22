# Stinerium UI Test Framework

A scalable **UI test automation framework** built on top of [Selenium WebDriver](https://www.selenium.dev/).  
Designed to create **maintainable, reusable, and efficient automated tests** for web applications.

## Features

- Cross-browser support (Chrome, Firefox, Edge).
- Built using the **Page Object Model (POM)** for clean architecture.
- Integrated reporting (Allure Reports / HTML reports).
- Easy execution both locally and in CI/CD pipelines (GitHub Actions, Jenkins, etc.).
- Configurable environments (DEV, TEST, STAGE, PROD).
- Parallel test execution support.

## Project Structure
```text
stinerium/
├── src/                      
│   ├── flow/                 
│   ├── pom/                  
│   ├── actions.py            
│   └── application_model.py 
├── utils/                
├── LICENSE.txt
├── setup.py
└── README.md
```

## Getting Started

### Prerequisites

- [Python 3.12+](https://www.python.org/)
- [Selenium WebDriver](https://pypi.org/project/selenium/)

### Installation

Clone the repository and install the dependencies:

```bash
pip install git+https://github.com/CoptarSoftware/stinerium.git
```
