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
stinerium/
├── src/ # Framework source code
│ ├── pages/ # Page Objects
│ ├── tests/ # Automated test cases
│ ├── utils/ # Utility classes and helpers
│ └── drivers/ # WebDriver configurations
├── reports/ # Generated test reports
├── config/ # Environment and test configuration files
├── requirements.txt # Python dependencies (if Python-based)
└── README.md

## Getting Started

### Prerequisites

- [Python 3.12+](https://www.python.org/)
- [Selenium WebDriver](https://pypi.org/project/selenium/)

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/CoptarSoftware/stinerium.git
cd stinerium
pip install -r requirements.txt
```
