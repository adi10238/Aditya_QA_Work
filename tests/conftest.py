import time

import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def setup_and_teardown(request):
    #global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    time.sleep(2)
    driver.quit()