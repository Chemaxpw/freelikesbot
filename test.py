from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("log-level=3") 
driver = webdriver.Chrome("./chromedriver",chrome_options=options)
driver.get("https://pikabu.ru/")
print(driver.title)
print(driver.find_element_by_css_selector("body").get_attribute('innerHTML'))
