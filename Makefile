APP_NAME=automation_test4
TAG=0.0.1

.PHONY: d_test
d_test:
	@docker compose exec test pytest -ra

.PHONY: d_test_api
d_test_api:
	@docker compose exec test pytest test/api

.PHONY: d_test_ui
d_test_ui:
	@docker compose exec test pytest test/ui

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
