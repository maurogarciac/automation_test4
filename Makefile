APP_NAME=automation_test4
TAG=0.0.1


## config doesn't really work as expected
# .PHONY: config
# config:
# 	ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
# 	export PYTHONPATH="$PYTHONPATH:$ROOT_DIR"
## maybe could pip install here too?

.PHONY: test
test:
	pytest -ra

.PHONY: test_api
test_api:
	pytest tests/api

.PHONY: test_ui
test_ui_f:
	pytest tests/ui --browser firefox

.PHONY: test_ui_headless
test_ui_f:
	pytest tests/ui --browser headless

.PHONY: clean
clean:
	find . | grep -E "(__pycache__|.\.pyc|.\.pyo)" | xargs rm -rf
