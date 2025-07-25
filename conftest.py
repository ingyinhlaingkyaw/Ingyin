from xml.dom.xmlbuilder import Options

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup_teardown():
    chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver

@pytest.fixture()
def login_as_admin(setup_teardown, username=None, password=None):
    driver = setup_teardown
    wait = WebDriverWait(driver, 10)
    name = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    name.send_keys("Admin")
    pword = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pword.send_keys("admin123")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()
    return driver