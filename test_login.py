import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username, password, expected",[
    ("Admin", "admin123", True),
    ("Admin","admin", False),
    ("admin","admin123", False),
    ("aaaa","aaaa", False),
])
def test_valid_login(username, password, expected,setup_teardown):
    driver = setup_teardown
    wait = WebDriverWait(driver, 10)
    name = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    name.send_keys(username)
    pword = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pword.send_keys(password)
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()

    if expected:
        assert "dashboard" in driver.current_url, "Login Failed"

    else:
        err_msg= wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
        assert "Invalid credentials" in err_msg.text, "login successful with invalid credentials"


def test_required_field(setup_teardown):
    assert True

def test_logout(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)
    user_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab")))
    user_icon.click()

    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']")))
    logout_btn.click()

    assert "login" in driver.current_url, "logout failed"

