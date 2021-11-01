from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #코드를 멈춰주는 모듈
import urllib.request #다운로드를 위한 모듈

chrome_path = r'/usr/local/bin/chromedriver' #chromedriver 경로를 못찾아줘서 별도로 지정함.
driver = webdriver.Chrome(executable_path=chrome_path) 
# driver = webdriver.Chrome('/usr/jeonsuhyeon/projects/selenium/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q") #검색창을 찾는 명령어
elem.send_keys('치즈웨이브') #검색어 입력
elem.send_keys(Keys.RETURN) #검색창 엔터
# driver.find_elements_by_css_selector('.rg_i.Q4LuWd')[0].click() #[0]로 가장 첫번째 항목을 선택하고 .click으로 클릭해주기
                                                                #개발자도구로 사진에 대한 class 확인 및 붙여넣기 
                                                                #여러개의 항목 선택시 find_element's' 를 사용

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight") #브라우저의 높이를 알 수 있는 코드

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #브라우저 끝까지 스크롤을 내리는 명령어

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME) #페이지 로딩을 기다려주는 코드

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:    
            driver.find_element_by_css_selector('.mye4qd').click() #더보기 항목을 클릭하기 위한 명령어
        except:
            break #더보기 항목이 없게되면 멈추기
    last_height = new_height

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2) #페이지를 로딩하는데 시간이 걸리므로 2초간 코드를 진행을 멈춰준다.
        imgUrl = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')  #이미지를 클릭했을때 나오는 세부이미지 class를 넣어주고 .get_attribute를 통해 src주소 다운로드 진행
                                                                                        #print된 src 주소 https://s3-ap-northeast-1.amazonaws.com/dcreviewsresized/20210117170120_photo1_5f3a51b4b5f9.jpg
        urllib.request.urlretrieve(imgUrl, str(count)+'.jpg') #src주소를 다운받아서 test.jpg라는 이름으로 저장해주는 명령어
        count = count + 1
    except:
        pass
driver.close()

"""
driver.find_element_by_css_selector('.n3VNCb') 처럼 class 이름을 통해 검색하게 될 경우 
동일한 이름의 여러 클래스가 나오는 경우도 있으니 좀 더 상세하게 하기 위해서는 
개발자 도구에서 class 우클릭 > copy > copy full XPath 를 선택한 후 
find_element_by_css_selector 대신에 find_element_by_xpath를 사용해준다.
find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
"""