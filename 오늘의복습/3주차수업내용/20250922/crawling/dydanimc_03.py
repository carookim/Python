# 동적 사이트에서 데이터를 크롤링 하는 방법

# pip install selenium webdriver-manager ^
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터 키등을 인렵하기 위해 사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

# 웹드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://auto.danawa.com/auto/?Work=record')
print('브라우저가 성공적으로 열렸습니다.')

# 사이트가 로드될때까지 기다린다.
time.sleep(1)
radio = driver.find_element(By.CSS_SELECTOR, "input[name='rdoMonthPeriod'][value='period']")
radio.click()
select = Select(driver.find_element(By.ID,'selMonthFrom'))
select.select_by_value('2024')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayFrom'))
select.select_by_value('01')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selMonthTo'))
select.select_by_value('2024')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayTo'))
select.select_by_value('12')

# 조회 버튼 클릭 #monthPeriodDiv > span:nth-child(2) > input[type=button]
# 속성중에 disable = True인 엘리먼트는 사용자 클릭을 막아놓음
# 이런 경우에는 강제로 실행 시키는 방법이 이거
btn = driver.find_element(By.XPATH,'//*[@id="monthPeriodDiv"]/span[2]/input')
driver.execute_script("arguments[0].click()",btn) # 사용자 마우스클릭 이벤트를 발생 ^
# driver.execute_script("selecRecord('period');") # 직접실행
# 최대 조회기간은 1년? ^ 예외처리 해보기 ^

time.sleep(3)
# 셀리니움 문법을 이용해서 원하는 태그의 속한 텍스트를 추출
soup = BeautifulSoup(driver.page_source,'html.parser')


time.sleep(10)

# 브라우저 종료
driver.quit()