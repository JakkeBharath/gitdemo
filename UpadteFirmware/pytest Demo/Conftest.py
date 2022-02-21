import py as py
from selenium import webdriver

import pytest


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Edge(executable_path="C:\Browser\msedgedriver.exe")
    driver.get("https://146.205.2.30/")
    driver.maximize_window()
    yield
    driver.close()

