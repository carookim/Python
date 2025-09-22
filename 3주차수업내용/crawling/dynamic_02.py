# dynamic_02.py 와 dynamic_02_1.py비교
# 여기 파일 dynamic_02.py는 월별로 선택이 순차적으로 하는
# 명령어가 있지만 1월만 바뀌고 브라우저가 닫히는 반면
# dynamic_02_1.py는 다 순차적으로 보여주고난뒤 브라우저가 닫히는 이유
# 둘다 for 문으로 월을 돌리고 있다. -> 월을 변경했을때 기다리는 시간을
# 추가해줘야한다. 여기서 time.sleep()으로 해결이 안되는 이유 도 알아보기 ^
# 1)
# 2)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://auto.danawa.com/auto/?Work=record'
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window() # 전체 화면으로 실행 : 옵션 사항
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
WebDriverWait(driver,10).until(
EC.presence_of_all_elements_located((By.CLASS_NAME,'recordSection'))
)
year_select = driver.find_element(By.ID,'selMonth')

# 객체로 만든다.
select_year = Select(year_select)
select_year.select_by_value('2024')
time.sleep(5)

# month_select_element = driver.find_element(By.ID,'selDay')
# select_month = Select(month_select_element)
# 1) for문 밖에 두면 작동을 하지않는 이유 ^
for i in range(1,13):
    month_select_element = driver.find_element(By.ID,'selDay')
    select_month = Select(month_select_element)
    select_month.select_by_value(f'{i:02}')
    # ^ f'{i:02}'

    # 2) 브라우저 지연 ^
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".recordTable.short tbody tr"))
    )


time.sleep(10)
driver.quit()