# Appium Python Mobile Automation Learning Project

A hands-on learning project for mobile test automation using Python, Appium, Pytest, and the Sauce Labs My Demo App Android application.

The project began with basic Appium tests and gradually developed into a small automation framework using Page Objects, reusable flows, test fixtures, screenshots, HTML reports, and GitHub Actions experimentation.

## What is covered

- Starting and validating an Android Appium session
- Locating elements with resource IDs, XPath, and UiAutomator selectors
- Explicit waits with Selenium expected conditions
- Product browsing, product details, scrolling, and sorting
- Login validation and logout flows
- Shopping cart items and quantities
- Multi-step checkout workflows and validation messages
- Page Object Model design
- Pytest fixtures and parameterized tests
- Failure screenshots and HTML test reports
- Local and CI-oriented Appium configuration
- Experimental Ollama, LangChain, Chroma, and RAG-based failure analysis

## Project structure

```text
.
├── config.py                    # Appium and Android configuration
├── conftest.py                  # Driver fixture, screenshots, and page fixtures
├── pytest.ini                   # Pytest discovery and reporting settings
├── requirements.txt             # Main Python test dependencies
├── data/                        # Test data and credentials
├── helpers/                     # Reusable end-to-end flows
├── pages/                       # Page Object Model classes
├── tests/                       # Appium/Pytest test cases
├── utils/                       # RAG and AI-assisted analysis experiments
├── .github/workflows/           # GitHub Actions workflow
└── mda-2.2.0-25.apk             # Sauce Labs demo application
```

## Prerequisites

- Python 3.10 or newer
- Java and Android SDK
- Android emulator or connected Android device
- Android platform tools with `adb`
- Node.js and npm
- Appium server with the UiAutomator2 driver
- Sauce Labs My Demo App APK

Verify that the device is visible:
-adb devices

Start Appium locally:
-appium

## Installation

Create and activate a virtual environment:
terminal/powershell
--> python -m venv .venv
--> .\.venv\Scripts\Activate.ps1

Install the main test dependencies:
-->python -m pip install -r requirements.txt

Install the Appium UiAutomator2 driver if needed:
-->appium driver install uiautomator2

## Running the tests
With the emulator/device and Appium server running:

'''powershell'''
-->python -m pytest

Run a specific test file:
-->python -m pytest tests/test_sample.py -v


Run only the Page Object tests:
--> python -m pytest tests/test_product_page_pom.py -v


Pytest is configured to create an HTML report at:
--> reports/report.html

Failure screenshots are saved under:
-->reports/screenshots/


## Configuration
Default local configuration is defined in `config.py`:

#text
Device: emulator-5554
Package: com.saucelabs.mydemoapp.android
Activity: com.saucelabs.mydemoapp.android.view.activities.SplashActivity
Appium server: http://localhost:4723


These values can be overridden with environment variables:

#powershell
$env:APPIUM_DEVICE = "emulator-5554"
$env:APPIUM_SERVER = "http://localhost:4723"
$env:APPIUM_APK = "mda-2.2.0-25.apk"

The driver fixture supports separate local and CI configuration through the `CI` environment variable.

## Page Object Model

Shared driver operations are implemented in `pages/base_page.py`. Screen-specific behavior is separated into page classes so that tests use these objects to keep test intent separate from locators and screen interaction details.

## Ollama and RAG experiments

The `utils` directory contains an experimental codebase assistant.

### `simple_rag.py`

Loads Python files into a large prompt and asks Ollama a question. This is useful for learning direct codebase prompting, although it does not perform retrieval from a vector database.

### `codebase_rag.py`

Implements a vector-based RAG workflow:

```text
Page Object files
    → document loading
    → text chunking
    → Ollama embeddings
    → Chroma vector store
    → relevant chunk retrieval
    → Ollama response
```

### Optional RAG dependencies

The RAG utilities are separate from the core Appium dependencies. Install them with:

```powershell
python -m pip install -U `
  langchain-ollama `
  langchain-core `
  langchain-community `
  langchain-text-splitters `
  langchain-chroma `
  chromadb
```

Install Ollama separately, start it, and download a chat model and an embedding model:

```powershell
ollama pull llama3.2
ollama pull qwen3-embedding
```

The chat model generates explanations. The embedding model converts source code into vectors for semantic retrieval. These should be treated as separate model roles.

The current RAG experiment primarily indexes files in `pages/` and persists its local vector data in `chroma_db/`.

## GitHub Actions

The workflow in `.github/workflows/appium.yml` experiments with:

- Python setup
- Android SDK setup
- APK download
- Appium installation
- Android emulator execution
- Pytest execution
- Failure artifact upload

CI execution may require additional maintenance as the Appium driver, APK filename, test dependencies, and artifact paths evolve.

## Current learning goals

- Improve test isolation and app-state reset behavior
- Add meaningful assertions to action-based tests
- Reduce duplicated navigation flows
- Improve locator stability
- Avoid broad exception handling that hides failures
- Separate optional AI dependencies from core test collection
- Expand RAG indexing to tests, helpers, fixtures, and configuration
- Add retrieval evaluation and source line metadata

## Project status

This is a personal learning project for me to learn how to use appium to test or automate a mobile application rather than a production automation framework. It documents the progression from introductory Appium tests to Page Object design, CI experimentation, and AI-assisted test failure analysis.
