# Automation Test 4
## Requirements

* Python 3.10.x installed

## Quick execution manual

1. Clone this Repository and change directory into it:
    ```shell
    git clone https://github.com/maurogarciac/automation_test4.git
    cd automation_test4
    ```
2. Create a Virtual Environment and name it `venv`:
    ```shell
    python -m venv venv
    ```
3. Activate the Environment:
    ```shell
    . venv/Scripts/activate
    ```
4. Install the required Packages:
    ```shell
    python -m pip install -r requirements.txt
    ``` 
5. Run tests by setting a browser as a parameter (firefox, chrome):
    ```shell
    python run_tests.py --browser firefox
    ```