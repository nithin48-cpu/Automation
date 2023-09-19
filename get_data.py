from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

tag = driver.find_element(By.ID, 'twotabsearchtextbox')
tag.send_keys('iphones')

button = driver.find_element(By.ID, "nav-search-submit-button")
button.click()
time.sleep(5)
driver.refresh()

# By.XPATH is a way to get tag by using such protocol

products = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
prices = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')

time.sleep(5)
print("Products Found : ", str(len(products)))
for i, j in zip(products, prices):
    print(i.text, "   ", j.text)
