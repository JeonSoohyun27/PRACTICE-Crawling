from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #코드를 멈춰주는 모듈
import urllib.request #다운로드를 위한 모듈

chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
# driver = webdriver.Chrome('/usr/jeonsuhyeon/projects/selenium/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q") #검색창을 찾는 명령어
elem.send_keys('치즈웨이브') #검색어 입력
elem.send_keys(Keys.RETURN) #검색창 엔터
# driver.find_elements_by_css_selector('.rg_i.Q4LuWd')[0].click() #[0]로 가장 첫번째 항목을 선택하고 .click으로 클릭해주기
                                                                #개발자도구로 사진에 대한 class 확인 및 붙여넣기 
                                                                #여러개의 항목 선택시 find_element's' 를 사용

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
count = 1
for image in images:
    image.click()
    time.sleep(2) #페이지를 로딩하는데 시간이 걸리므로 2초간 코드를 진행을 멈춰준다.
    imgUrl = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')  #이미지를 클릭했을때 나오는 세부이미지 class를 넣어주고 .get_attribute를 통해 src주소 다운로드 진행
                                                                            #print된 src 주소 https://s3-ap-northeast-1.amazonaws.com/dcreviewsresized/20210117170120_photo1_5f3a51b4b5f9.jpg
    urllib.request.urlretrieve(imgUrl, str(count)+'.jpg') #src주소를 다운받아서 test.jpg라는 이름으로 저장해주는 명령어
    count = count + 1

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_path)
