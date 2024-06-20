APP_NAME=automation_test4
TAG=0.0.1

.PHONY: d_test
d_test:
	docker-compose up

.PHONY: test_api
test_api:
	pytest tests/api

.PHONY: test_ui_f
test_ui_f:
	pytest tests/ui --browser firefox

.PHONY: test_ui_hl
test_ui_c:
	pytest tests/ui --browser chrome

.PHONY: clean
clean:
	find . | grep -E "(__pycache__|.\.pyc|.\.pyo)" | xargs rm -rf
