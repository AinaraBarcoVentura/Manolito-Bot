from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

WINDOW_SIZE="800,600"

def init_driver(server):
	chrome_options = Options()
	#chrome_options.add_argument("--headless")  
	chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

	driver = None

	''' THIS IS ONLY FOR SERVER '''
	if server==1:
		chrome_options.binary_location = GOOGLE_CHROME_BIN
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--no-sandbox')
		driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
	else:
		driver = webdriver.Chrome(executable_path=r'C:/Users/rma/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)

	return driver

def find(search_word, runType):
	driver = init_driver(runType)
	driver.get("http://hdfull.tv/")
	elem = driver.find_element_by_id("search-query")
	elem.send_keys(search_word)
	elem.send_keys(Keys.RETURN)

	peliculas = driver.find_elements_by_class_name('spec-border-ie')
	dict = {}

	for i in peliculas:
		link = i.get_attribute('href')
		name = i.find_element_by_class_name('img-preview').get_attribute('title')
		dict[name] = link

	driver.close()
	return dict	
'''
res = int(input())

driver.get(peliculas[res-1].get_attribute('href'))

allresult = driver.find_elements_by_class_name('embed-selector')

for i in allresult:
	info = i.find_elements_by_css_selector('h5.left > span')
	button = i.find_element_by_class_name('icon-share-alt')
	linkext = button.find_element_by_xpath('..').get_attribute('href')
	print(info[0].text + " " + info[1].text + " "+ info[2].text)


driver.get(linkext)
elem = driver.find_element_by_id('external-link')
linkfinal = elem.get_attribute('href')

print(linkfinal)
'''

