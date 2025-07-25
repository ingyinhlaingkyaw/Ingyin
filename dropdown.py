import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

chrome_driver_path = "/Users/ingyin.ihk/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID,"dropdown")
dropdown = Select(dropdown_element)

#get all options
options = dropdown.options
option_text = [opt.text for opt in options]

#selet option 1
#dropdown.select_by_value("1")
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Option 1")
selected_text = dropdown.first_selected_option.text

assert "Option 1" in selected_text, "Error Message"




