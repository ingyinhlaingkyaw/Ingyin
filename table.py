import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/tables")

table1 = driver.find_element(By.ID, "table1")
assert table1.is_displayed(), "Table 1 is not displayed"

#print table header
headers = driver.find_elements(By.XPATH, "//*[@id='table1']/thead/tr/th")
header_names = [header.text.strip() for header in headers]
print("Headers:", header_names)

#print each row data
rows = driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr")
for i,row in enumerate(rows):
    cols = row.find_elements(By.TAG_NAME,"td")
    row_data = [col.text.strip() for col in cols]
    print(f"Row {i+1}:" , row_data)

