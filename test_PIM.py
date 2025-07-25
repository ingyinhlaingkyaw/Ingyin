import os.path
import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import take_screenshot


@allure.feature("Personal Detail")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_em(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver,10)
    #go to PIM module
    try:
        with allure.step("Go to PIM Module"):
            PIM = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
            PIM.click()

        #add button
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
        add_btn.click()

        with allure.step("Enter Employee Detail"):
            #first name
            firstname = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
            firstname.send_keys("Nang")

            #middle name
            middle_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Middle Name']")))
            middle_name.send_keys("Kham")

            #last name
            last_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
            last_name.send_keys("Laung")

        #upload employee image
        #1. find >>input type = "file"
        #2. abspath >> os.path.abspath("file location")
        #3. send_keys
        with allure.step("Upload Employee Image"):
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
            img_source = os.path.abspath("./resources/1.png")
            file_input.send_keys(img_source)

        #confirm upload
        uploaded_pic = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "employee-image"))).get_attribute("src")
        assert "/web/images/default-photo.png" not in uploaded_pic, "image upload fail"

        #save button
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_btn.click()

        #confirm save employee
        toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
        assert toast.is_displayed(), "employee not added successfully"
    except Exception as e:
        take_screenshot(driver, "error.png")
        allure.attach.file(f"screenshot/error_emp.png", name="failure screenshot")
        attachment_type = allure.attachment_type.PNG
        raise e


def search_employee(driver, wait, employee_name):
    PIM = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
    PIM.click()

    search_username = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Employee Name']/following::div/input")))
    search_username.send_keys(employee_name)

    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    search_btn.click()

    name_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Nang')]")))
    assert name_element.is_displayed(), "Employee is not found "

def test_edit_employee(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)

    search_employee(driver, wait, "Nang")

    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-container']//button[1]")))
    edit_icon.click()

    #driver license no
    licenseNo = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'License Number')]/following::div/input")))
    licenseNo.clear()
    licenseNo.send_keys("OK0011011")

    #license expire date
    license_exp = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='License Expiry Date']/following::input[1]")))
    license_exp.clear()
    license_exp.send_keys("2029-01-01")

    #nationality
    nationality = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='Nationality']/following::div")))
    nationality.click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Serbian']"))).click()

    #marital status
    marital_status = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Marital Status']/following::div[1]")))
    ActionChains(driver).move_to_element(marital_status).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    #date of birth
    dob = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Date of Birth']/following::input[1]")))
    dob.clear()
    dob.send_keys("1994-01-01")

    #gender
    #female radio
    female_radio = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Female']")))
    if not female_radio.is_selected():
        female_radio.click()

    #save button
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and normalize-space()='Save']")))
    save_btn.click()

    # confirm save employee
    toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast.is_displayed(), "employee not update successfully"

def test_upload_file(login_as_admin):
    driver = login_as_admin
    wait = WebDriverWait(driver, 10)

    search_employee(driver, wait, "Nang")

    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-container']//button[1]")))
    edit_icon.click()

    #add button
    add_btn= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_btn.click()

    #file input
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_path = os.path.abspath("./resources/ecommerce_test_plan.pdf")
    file_input.send_keys(file_path)

    #save btn
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']")))
    save_btn.click()

    # confirm save employee
    toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Successfully')]")))
    assert toast.is_displayed(), "employee not update successfully"

    #confirm upload
    file_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'ecommerce_test_plan.pdf')]")))
    assert file_name.is_displayed(),"file upload not successful"

def test_download_file(tmp_path):
    #use temporary folder
    download_dir = str(tmp_path)

    chrome_option = Options()
    chrome_option.add_experimental_option("prefs", {
        "download.default_directory":download_dir,
        "download.prompt_for_download":False,
        "safebrowsing.enabled":True
    })
    service = Service("/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options= chrome_option)

    wait = WebDriverWait(driver,10)
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        name = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        name.send_keys("Admin")
        pword = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        pword.send_keys("admin123")
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_btn.click()

        time.sleep(3)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/128")

        time.sleep(5)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-download']")))
        download_button.click()

        time.sleep(5)
        #verify if file exist in download directory
        download_file= os.listdir(download_dir)
        assert len(download_file)>0, "file download fail"

        #check the file and file type
        time.sleep(5)
        download_file_path = os.path.join(download_dir, download_file[0])
        print(f"File download successfully to: {download_file_path}")

        assert os.path.isfile(download_file_path), "download file is missing"
    finally:
        driver.quit()

