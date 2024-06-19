# Automation Test 4 (pytest implementation)

Just a simple test automation framework with pytest that supports ui and api tests

## Requirements

* Python 3.12 installed
* Make installed

## Quick installation steps

1. Clone this Repository and change directory into it:
    ```shell
    git clone https://github.com/maurogarciac/automation_test4.git
    cd automation_test4
    ```
2. Create a Virtual Environment and name it `.venv`:
    ```shell
    python -m venv .venv
    ```
3. Activate the Environment:
    ```shell
    .venv/Scripts/activate
    ```
    ```shell
    source .venv/Scripts/activate
    ```
4. Install the required Packages:
    ```shell
    python -m pip install -r requirements.txt
    ``` 
5. Run tests:

    ### Flags for execution:
        An optional '--browser' flag can be included after 'pytest' to specify the browser option (default is 'chrome'):
        - firefox
        - chrome_headless
        - remote (not working, requires remote-wd setup)

    1. api tests
    2. ui tests
    3. all tests 
    
    - With make:
        ```shell
        make test_api
        make test_ui
        make test
        ```
    - Manually:
        ```shell
        pytest tests/api
        pytest tests/ui
        pytest 
        ```

## To do:

1. Fix config in makefile to sort out import issues
2. Add more tests