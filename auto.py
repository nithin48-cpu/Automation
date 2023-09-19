# from selenium.webdriver import Chrome
# import time
#
# driver = Chrome()
# driver.get("https://www.google.com/")
# time.sleep(10)
# # button=driver.find_element('class','T-I T-I-KE L3')
# # button.click()
# # time.sleep(5)
#
#
# tag = driver.find_element('class', 'gLFyf')
# tag.send_keys('selenium')


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