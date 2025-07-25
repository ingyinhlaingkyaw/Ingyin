from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
print("main window handle:", driver.current_window_handle)

driver.execute_script("window.open ('https://demoqa.com/checkbox', '_blank');")

all_handles = driver.window_handles
print("All window handle:" , all_handles)

driver.switch_to.window(all_handles[1])
print("switched to:", driver.title)

driver.switch_to.window(all_handles[0])
print("back to:", driver.title)

driver.quit()

