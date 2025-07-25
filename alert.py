import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
js_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
js_alert.click()
#actions = ActionChains(driver)
#actions.double_click(js_alert)
#actions.context_click(js_alert)
alert = driver.switch_to.alert
alert.accept()
time.sleep(5)

confirm_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_alert.click()
con_alert = driver.switch_to.alert
con_alert.dismiss()
time.sleep(5)

prompt_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_alert.click()
pro_alert = driver.switch_to.alert
pro_alert.send_keys("555555")
pro_alert.accept()
time.sleep(5)
