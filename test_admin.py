import time
from urllib.parse import uses_relative

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username, password, confirm_password,error_msg",[
    ("lily1", "admin123", "admin123", []),
    ("lily", "admin123", "admin123", ["Should be at least 5 characters"]),
    ("lily2", "admin","admin", ["Should have at least 7 characters"]),
    ("lily3", "admin123", "admin", ["Passwords do not match"]),
    ("lily4", "admin123", "admin123", []),
    ("","","", ["Required"])
])
def test_add_admin(login_as_admin,username,password,confirm_password,error_msg):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)
    admin_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin")))
    admin_tab.click()

    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_btn.click()

    #user role
    user_role = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='User Role']/following::div[1]")))
    actions = ActionChains(driver)
    actions.move_to_element(user_role).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    #employee name
    em_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
    em_name.send_keys("em")
    time.sleep(4)
    ActionChains(driver).move_to_element(em_name).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    #status
    status = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Status']/following::div[1]")))
    status.click()
    enable_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Enabled']")))
    enable_option.click()

    #username
    username1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    username1.send_keys(username)

    #password
    password1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following::div[1]/input")))
    password1.send_keys(password)

    #confirm password
    com_pass = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::div[1]/input")))
    com_pass.send_keys(confirm_password)

    #click save btn
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    save_btn.click()

    #if expected error message displayed, validate
    if error_msg:
        for error in error_msg:
            msg = wait.until(EC.visibility_of_element_located((By.XPATH,f"//span[normalize-space()='{error}']")))
            assert msg.is_displayed(), "Expected error message is not displayed"
    else:
        toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
        assert toast.is_displayed(), "Admin user not added successfully"

def test_search_admin(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)
    # Click on Admin tab
    admin_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin")))
    admin_tab.click()

    # Search by username
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    username_input.send_keys("Jobinsam@6742")

    form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-form")))
    form.submit()

    # Click edit icon
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Jobinsam@6742')]")))
    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")))
    edit_icon.click()

    # Wait for the username field to become editable
    username_edit = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    time.sleep(5)

    # Clear username via keyboard
    username_edit.send_keys(Keys.COMMAND+"a")
    username_edit.send_keys(Keys.DELETE)
    username_edit.send_keys("EmilyJanes")

    # 🧠 WAIT for checkbox to APPEAR in DOM after toggle
    checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Yes']//following-sibling::input")))
    driver.execute_script("arguments[0].click();", checkbox)

    # Enter password
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following::div[1]/input")))
    password_input.send_keys("password123")

    confirm_password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::div[1]/input")))
    confirm_password_input.send_keys("password123")

    time.sleep(5)
    # Click Save
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    save_button.click()

    # Verify toast
    toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast.is_displayed(), "Update is not successful"

    #Home work

@pytest.mark.parametrize("username", [
    "lily1",
    "lily4"
])

def test_delete_admin(login_as_admin, username):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)

    admin_tab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin")))
    admin_tab.click()

    # Search by username
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::div[1]/input")))
    username_input.send_keys(username)
    time.sleep(3)

    form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-form")))
    form.submit()

    wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{username}')]")))
    delete_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']")))
    delete_icon.click()

    del_yes = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
    del_yes.click()

    toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast.is_displayed(), "User Delete Failed"

    # '''
    # Home Work (Delete)
    #  1. search employee
    #  2. click delete button
    #  3. confirm, cancel
    #  4. assert
    #  '''


