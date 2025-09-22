# 수강생 작성 (1)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

url = 'https://auto.danawa.com/auto/?Work=record'

#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window()
print('사이트 접속했습니다.')

# 사이트가 로드될때까지 기다린다.
time.sleep(1)

# 메인 화면에서 신차 -> 판매실적 -> 기간선택 -> 2024년 9월부터 2025년도 9월달까지 -> 조회
# 그러고 나서 정보 문자열 추출

# 신차 클릭 newcar
# newcar_click = driver.find_element(By.CLASS_NAME,'gnb__col gnb__newcar') # ^
newcar_click = driver.find_element(By.XPATH,'//*[@id="gnbMenu"]/div/div/div[2]')
newcar_click.click()
time.sleep(2)

# 판매 실적 클릭 sellperformance
# sellperformance_click = driver.find_element(By.CLASS_NAME,'item on') # ^
sellperformance_click = driver.find_element(By.XPATH,'//*[@id="autodanawa_gridC"]/div[1]/ul/li[3]')
sellperformance_click.click()
time.sleep(2)

# 레디오 박스, 기간선택 24/09 - 25/09
# 기간선택 레디오 버튼
radio =  driver.find_element(By.CSS_SELECTOR,"input[name='rdoMonthPeriod'][value='period']")
radio.click()
time.sleep(1)

select = Select(driver.find_element(By.ID,'selMonthFrom'))
select.select_by_value('2024')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayFrom'))
select.select_by_value('09')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selMonthTo'))
select.select_by_value('2025')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayTo'))
select.select_by_value('09')

# 조회
btn = driver.find_element(By.XPATH,'//*[@id="monthPeriodDiv"]/span[2]/input')
driver.execute_script("selectRecord('period');")

time.sleep(3)

# 해당 정보를 담은 문자열 추출 ^
soup = BeautifulSoup(driver.page_source,'html.parser')
car_datas = soup.select('#autodanawa_gridC > div.gridMain > article > main > div > div:nth-child(4) > div.left > table > tr')
for row in car_datas:
    car_datas = row.select('td')
    print(car_datas[0].text.strip(),
        car_datas[1].text.strip(),
        car_datas[2].text.strip()
        )