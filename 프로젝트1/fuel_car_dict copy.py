# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터 키등을 입력하기 위해 사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 웹드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://stat.eseoul.go.kr/statHtml/statHtml.do?orgId=201&tblId=DT_201004_I020004&conn_path=I2&obj_var_id=&up_itm_id=')
driver.maximize_window()
print('브라우저가 성공적으로 열렸습니다.')
time.sleep(3)

# 시점 -> 시작 지점 -> 2015.01

# 시점 클릭
point_click = driver.find_element(By.ID,'tabTimeText')
point_click.click()
time.sleep(2)

# 2015.12 클릭
y2020_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]/option[109]')
y2020_m01_click.click()
time.sleep(2)

# 2024.12 클릭
y2020_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[2]/option[1]')
y2020_m01_click.click()
time.sleep(2)

# 조회 v 클릭
y2025_m01_click = driver.find_element(By.XPATH,'//*[@id="tabTimeText"]/button[2]')
y2025_m01_click.click()
time.sleep(10)

# 해당 정보를 담은 문자열 추출
soup = BeautifulSoup(driver.page_source,'html.parser')
fuel_car_datas = soup.select('#mainTable > tbody > tr')

for i, row in enumerate(fuel_car_datas[:5]): # 상위 5행만 처리 range(0,4)
    text = row.text.strip()  # 행의 텍스트 추출
    cells = text.split('\xa0')  # 띄어쓰기 기준으로 분리
    if i == 0:
        list_subtotal = cells
    elif i == 1:
        list_passenger = cells
    elif i == 2:
        list_bus = cells
    elif i == 3:
        list_truck = cells
    elif i == 4:
        list_special = cells
    # 연료별 총합 리스트 만들지 않고 일단 진행하고 있다.

# 리스트 컴프리헨션으로  '-'를 '0'으로 변경
change_0 = [list_subtotal,list_passenger,list_bus,list_truck,list_special]
list_subtotal = ['0' if x == '-' else x for x in change_0[0]]
list_passenger = ['0' if x == '-' else x for x in change_0[1]]
list_bus = ['0' if x == '-' else x for x in change_0[2]]
list_truck = ['0' if x == '-' else x for x in change_0[3]]
list_special = ['0' if x == '-' else x for x in change_0[4]]

# zip()으로 리스트들의 동일한 인덱스끼리 튜플로 묶기
list_subtotal = list_subtotal[1:] # 계 소계로 되어있어서 인덱스 하나가 밀린다. 그래서 인덱스 1부터 시작하게 한다.
fuel_messy_datas = list(zip(list_subtotal,list_passenger,list_bus,list_truck,list_special))
# print(fuel_messy_datas)

# 처음 0만 car_type / 소계 - 휘발유 - 전기 - CNG - 하이브리드 - 수소 - 기타
# 후에는 저렇게 반복하며 소계_list, 휘발유_list ....에 삽입
차종별_list = []
소계_list = []
휘발유_list = []
경유_list = []
LPG_list = []
전기_list = []
CNG_list = []
하이브리드_list = []
수소_list = []
기타_list = []

pattern_list_2 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]
for i, data in enumerate(fuel_messy_datas):
    if i == 0:
        차종별_list.append(fuel_messy_datas[i])
    else:
        idx = (i - 1) % len(pattern_list_2) # 기존 인덱스 에서 1을 빼고 , 9로 나눈 나머지를 idx로 사용
        pattern_list_2[idx].append(data)

pattern_list_3 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]

# 검토
# print(소계_list) O
# print(휘발유_list) O
# print(경유_list) O
# print(전기_list) O
# print(CNG_list) O
# print(하이브리드_list) O
# print(수소_list) O
# print(기타_list) O

# 표시
# print('*'*100)

little_query = []


# 연월 리스트 만들기 (2015-01 ~ 2024-12)
from datetime import datetime

dates = []
for year in range(2024, 2014, -1):
    for month in range(12, 0, -1):  # 12월부터 1월까지
        dates.append(f"{year}{month:02d}") # 02d 는 한자리 월수 1,2,3 .. 등을 01,02,03.. 으로 입력되게 설정

# 검토
# print(dates)

# 필요한 만큼 슬라이싱 하기
# print(dates[:len(dates)-11]) # 확인
ym = dates[:len(dates)-11]



pattern_list_4 = ['승용차', '승합차', '화물차', '특수차']
pattern_list_5 = ['휘발유','경유','LPG','전기','CNG','하이브리드','수소','기타']

