from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

#################################Настройки###################################

LIKES_TIMES = 10				#Выполнений задания "Поставить лайк" подряд
VIEWS_TIMES = 10 				#Выполнений задания "Посмотреть видео" подряд
HEADLESS_MODE = True		    #Скрытый режим (True или False)
MUTE_AUDIO = True				#Отключить звук (True или False)

#############################################################################

if __name__ == "__main__":
	if len (sys.argv) < 2:
		print("Недостаточно параметров")
		sys.exit()
	LOGIN = sys.argv[1]
	PASSWORD = sys.argv[2]
	
def login():
	print("\n Вход на сайт...")
	driver.get("http://freelikes.online/")
	get_element(".socico.ytico").click()
	get_element("#identifierId").send_keys(LOGIN)
	get_element(".CwaK9").click()
	get_element(".whsOnd.zHQkBf").send_keys(PASSWORD)
	get_element(".CwaK9").click()
	sleep(3)
	
def bot_like():
	print("\n Накрутка лайков")
	window_freelikes = driver.window_handles[0]
	last_task = ""
	repeat = 0
	need_delete = False
	
	for i in range(LIKES_TIMES):
		driver.get("http://freelikes.online/earn/youtube/ytlike")
		print(" "+str(i+1)+": "+get_element("font#points2").text)
		task_element = get_element(".col-sm-12") 
		if task_element is None:
			print("  Нет заданий") #debug
			return True
		task = task_element.get_attribute("id")
		print(task)
		if task == last_task:
			repeat += 1
			print("  Повтор задания: "+str(repeat)) #debug
			if repeat > 2:
				driver.find_element_by_class_name("delete").click()
				print("  Удаление задания") #debug
				repeat = 0
				continue
		else:
			task = last_task
			repeat = 0
		driver.find_element_by_class_name("col-sm-3").click()
		window_youtube = driver.window_handles[1]
		driver.switch_to.window(window_youtube)
		like_button = get_element("yt-icon.style-scope.ytd-toggle-button-renderer")
		if like_button is not None:
			like_button.click()
			sleep(4)
		else:
			print("  Кнопка лайка не найдена") #debug
			need_delete = True
		driver.close()
		driver.switch_to.window(window_freelikes)
		if need_delete:
			driver.find_element_by_class_name("delete").click()
			print("  Удаление задания") #debug
			need_delete = False
		sleep(2)

	return False

def bot_view():
	print("\n Накрутка просмотров")
	window_freelikes = driver.window_handles[0]
	need_delete = False
	
	for i in range(VIEWS_TIMES):
		driver.get("http://freelikes.online/earn/youtube/ytview")
		print(" "+str(i+1)+": "+get_element("font#points2").text)
		task = get_element(".col-sm-3")
		if task is None:
			print("  Нет заданий") #debug
			return True
		task.click()
		window_youtube = driver.window_handles[1]
		driver.switch_to.window(window_youtube)
		if check_blacklist(driver.current_url):
			need_delete = True
		else:
			sleep(31)
		driver.close()
		driver.switch_to.window(window_freelikes)
		if need_delete:
			driver.find_element_by_class_name("delete").click()
			print("  Удаление задания") #debug
			need_delete = False
		sleep(2)

	return False

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
	
def check_blacklist(url):
	blacklist = [
		"https://www.youtube.com/watch?v=xrVUQ-KKra8",
		"https://www.youtube.com/watch?v=1Mlb7BjYnaI",
		"https://www.youtube.com/watch?v=EK4CVx-1SmY",
		"https://www.youtube.com/watch?v=BpT0s7sg_VU"
	]
	return url in blacklist
	
	
def bot():
	while True:
		likes_empty = bot_like() 
		views_empty = bot_view()
		if likes_empty and views_empty:
			print("\n Задания закончились, ждём 10 минут")
			sleep(600)

def main():
	login()
	bot()

options = webdriver.ChromeOptions()
if HEADLESS_MODE: options.add_argument('--headless')
if MUTE_AUDIO: options.add_argument("--mute-audio") 
#options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3") 
driver = webdriver.Chrome("./chromedriver",chrome_options=options)
main()

	
