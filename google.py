from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
# driver = webdriver.Chrome('/usr/jeonsuhyeon/projects/selenium/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q") #검색창을 찾는 명령어
elem.send_keys('치즈웨이브')
elem.send_keys(Keys.RETURN)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_path)
