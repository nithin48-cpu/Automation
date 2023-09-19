from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
tag = driver.find_element(By.CLASS_NAME, 'gLFyf')
tag.send_keys('selenium')
time.sleep(5)

button = driver.find_element(By.CLASS_NAME,'gNO89b')
button.click()
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.quit()
