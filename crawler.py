import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 셀레늄 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)  # seconds
driver.get('https://ucheck.mju.ac.kr/')

# 로그인
driver.find_element(By.NAME, 'id').send_keys('60221348')
driver.find_element(By.NAME, 'passwrd').send_keys('xorkd1004!')
driver.find_element(By.ID, 'loginButton').click()

# 로딩 대기
time.sleep(3)  # seconds

# td 태그 안 text 가져오기
list_item = driver.find_elements(By.TAG_NAME, 'td')

string = ''
data = []

# 구분자 ,로 string 저장
for e in list_item:
    string += e.text + ','

data = string.split(',,')

# 맨 뒤 의미 없는 값 제거
data = data[0:-2]

print(data)
