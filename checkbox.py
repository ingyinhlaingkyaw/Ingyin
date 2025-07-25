import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")


checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checkbox[0].click()

print("initial state of checkbox")
for i,cb in enumerate(checkbox):
    print(f"Checkbox {i+1} is selected: {cb.is_selected()}")


