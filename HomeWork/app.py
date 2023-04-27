from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('http://www.rozetka.ua')
