import subprocess
import uuid
import os

import allure
import chromedriver_autoinstaller
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

status = None


@pytest.fixture(scope="session", autouse=True)
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_experimental_option("detach", True)
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    base_dir = os.path.dirname(__file__)
    results_dir = os.path.join(base_dir, 'allure-results')
    report_dir = os.path.join(base_dir, 'allure-report')

    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    command = ['allure', 'generate', results_dir, '-o', report_dir, '--clean']
    subprocess.run(command, check=True)