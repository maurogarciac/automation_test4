import os
from datetime import datetime

import pytest


# Global test configuration file
def pytest_addoption(parser):  # Reads flags and options
    parser.addoption("--browser", action="store", default="chrome_headless", help="browser to execute the automation")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = f"reports/report-{datetime.now().strftime('%Y-%b-%d-%H:%M')}.html"
