# Automation Test 4 (pytest implementation)

Just a simple test automation framework with pytest that supports ui and api tests

## Requirements:

* Python 3.12 installed

## Optional requirements (do yourself a favor):

* Make 4.4.1 (or compatible version)
* Docker 26.1.1 (or compatible version)

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
   To run all the tests, just run `pytest` in local env or `make test` for docker container.

    ### Flags for execution:
        An optional '--browser' flag can be included after 'pytest' to specify the browser option (default is 'chrome'):
        - firefox
        - chrome_headless
        - remote (not working, requires remote-wd setup)

    1. api tests
    2. ui tests

    - Locally with pytest:
        ```shell
        pytest tests/api
        pytest tests/ui
        ```
    - Locally with Make:
        ```shell
        make test_ui_f
        make test_ui_hl
        ```

    - With Docker:
        ```shell
        make d_test
        make d_test_api
        make d_test_ui_hl
        ```

## To do:

1. Add docker support
2. Solve report generation issue (not generating rn)
3. Add more tests