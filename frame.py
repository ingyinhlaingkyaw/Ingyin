import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)

driver.switch_to.frame("mce_0_ifr")

editor = driver.find_element(By.ID, value="tinymce")
#editor.clear()
editor.send_keys("test")

