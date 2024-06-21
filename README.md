# Asapp Challenge by Mauro Garcia

Just a simple test automation framework with pytest that supports ui and api tests

## Requirements:

* Python 3.12

## Optional *recommended* requirements:

* Make 4.4.1
* Docker 26.1.1
* docker-compose 2.27

## Local setup steps:

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
    - Linux
    ```shell
    chmod +x .venv/Scripts/activate
    .venv/Scripts/activate
    ```
    - MacOs
    ```shell
    source .venv/Scripts/activate
    ```
4. Install the required Packages:
    ```shell
    python -m pip install -r requirements.txt
    ``` 
5. Create an *.env* file with the contents of *.env.example*

## Docker setup steps:
1. Clone this Repository and change directory into it:
    ```shell
    git clone https://github.com/maurogarciac/automation_test4.git
    cd automation_test4
    ```

2. Either run `docker-compose up` or `make d_test`

## Run tests:  
To run all the tests, just run `pytest` in local env or `make d_test` for docker container.  

### Flags for execution:
An optional `--browser` flag can be included after `pytest` to specify the browser option (defaults to *chrome*):  

> * chrome
> * firefox
> * chrome_headless
> * remote (not working currently, requires remote-wd setup)
    
#### These are the commands to run the test groups, __api__ and __ui__: 

- Locally with pytest:
    ```shell
    pytest tests/api
    pytest tests/ui
    ```
- Locally with Make (to run in visual browsers):
    ```shell
    make test_ui_f
    make test_ui_c
    ```

## To do:

1. Add page objects for cart page
2. Add UI tests
3. Add API tests
4. Export reports from docker container to docker-reports directory
5. Implement pytest-parallel?