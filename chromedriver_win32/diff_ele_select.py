from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver=Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

tag = driver.find_element(By.ID,'twotabsearchtextbox')
tag.send_keys('iphones')

button = driver.find_element(By.ID,"nav-search-submit-button")
button.click()

driver.refresh()



