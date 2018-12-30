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
print(driver.current_url)
get_element("#identifierId").send_keys("markata89")
print(driver.current_url)
get_element(".CwaK9").click()
print(driver.current_url)
get_element(".whsOnd.zHQkBf").send_keys("rvtrbtrb564565")
print(driver.current_url)
get_element(".CwaK9").click()
sleep(3)
driver.get("http://freelikes.online/earn/youtube/ytlike")
print(driver.current_url)
try:
	balance = get_element("font#points2").text
except:
	print("Not found")
else:
	print(balance)
