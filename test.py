from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_element(selector):
	for i in range(4):
		sleep(2)
		try:
			element = driver.find_element_by_css_selector(selector)
		except:
			pass
		else:
			return element
	return None

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("log-level=3") 
driver = webdriver.Chrome("./chromedriver",chrome_options=options)
driver.get("http://freelikes.online/")
get_element(".socico.ytico").click()
get_element("#identifierId").send_keys("markata89")
get_element(".CwaK9").click()
get_element(".whsOnd.zHQkBf").send_keys("dhfd7fhd7f8")
get_element(".CwaK9").click()
sleep(3)
get_element("#profileIdentifier").click()
sleep(2)
try:
	balance = get_element("font#points2").text
except:
	print("Not found")
else:
	print(balance)
