APP_NAME=automation_test4
TAG=0.0.1


## config doesn't really work as expected
# .PHONY: local_config
# local_config:
# 	ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
# 	export PYTHONPATH="$PYTHONPATH:$ROOT_DIR"
## maybe could pip install here too?

.PHONY: d_test
d_test:
	@Docker pytest -ra

.PHONY: d_test_api
d_test_api:
	@Docker pytest test/api

.PHONY: d_test_ui_hl
d_test_ui_hl:
	@Docker pytest test/ui --browser chrome_headless

.PHONY: test_api
test_api:
	pytest tests/api

.PHONY: test_ui_f
test_ui_f:
	pytest tests/ui --browser firefox

.PHONY: test_ui_hl
test_ui_hl:
	pytest tests/ui --browser chrome_headless

.PHONY: clean
clean:
	find . | grep -E "(__pycache__|.\.pyc|.\.pyo)" | xargs rm -rf
