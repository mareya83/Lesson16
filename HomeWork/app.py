from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('http://www.rozetka.ua')

time.sleep(5)

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Samsung")

time.sleep(5)

ActionChains(driver).key_down(Keys.ENTER).perform()

time.sleep(5)