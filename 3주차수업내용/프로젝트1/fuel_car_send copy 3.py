# 수소가 사라지는 시기 를 제외하고 일단 작동 시키는 중
# 2015.01 -> 2015.12

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

# 시점 -> 시작 지점 -> 2015.12 -> 2024.12

# 시점 클릭
point_click = driver.find_element(By.ID,'tabTimeText')
point_click.click()
time.sleep(2)

# 2015.12 클릭
start_point_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]')
start_point_click.click()
time.sleep(2)

# 2024.12 클릭
y2020_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]/option[120]')
y2020_m01_click.click()
time.sleep(2)

# 조회 v 클릭
y2025_m01_click = driver.find_element(By.XPATH,'//*[@id="tabTimeText"]/button[2]')
y2025_m01_click.click()
time.sleep(10)

# 해당 정보를 담은 문자열 추출 (4)
soup = BeautifulSoup(driver.page_source,'html.parser')
fuel_car_datas = soup.select('#mainTable > tbody > tr')

# 행 별로 저장
for i, row in enumerate(fuel_car_datas[:5]): # 상위 5행만 처리 range(0,4)
    text = row.text.strip()  # 행의 텍스트 추출
    cells = text.split('\xa0')  # \xa0 기준으로 분리
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

# 저장된 데이터 내부에 있는 '-'를 '0'으로 리스트 컴프리헨션으로 변경
change_0 = [list_subtotal,list_passenger,list_bus,list_truck,list_special]
list_subtotal = ['0' if x == '-' else x for x in change_0[0]]
list_passenger = ['0' if x == '-' else x for x in change_0[1]]
list_bus = ['0' if x == '-' else x for x in change_0[2]]
list_truck = ['0' if x == '-' else x for x in change_0[3]]
list_special = ['0' if x == '-' else x for x in change_0[4]]

# 1. 각 리스트에서 순수한 '값'만 추출합니다.
# 데이터가 [헤더, 값, 헤더, 값, ...] 형태로 반복되므로, 인덱스 1부터 2칸씩 건너뛰며 값을 가져옵니다.
values_subtotal = list_subtotal[1::2]
values_passenger = list_passenger[1::2]
values_bus = list_bus[1::2]
values_truck = list_truck[1::2]
values_special = list_special[1::2]

# 2. 값 리스트들을 zip으로 묶어 데이터를 '열' 기준으로 재구성합니다.
# 이제 fuel_messy_datas의 각 튜플은 특정 시점의 특정 연료에 대한 차종별 데이터 묶음이 됩니다.
fuel_messy_datas = list(zip(values_subtotal, values_passenger, values_bus, values_truck, values_special))

# 열로 저장된 데이터를 각 연료별 리스트에 분배합니다.
차종별_list = [] # 이 리스트는 이제 사용되지 않으므로 비워두거나 삭제해도 됩니다.
소계_list = []
휘발유_list = []
경유_list = []
LPG_list = []
전기_list = []
CNG_list = []
하이브리드_list = []
수소_list = []
기타_list = []

pattern_list_2 = [소계_list, 휘발유_list, 경유_list, LPG_list, 전기_list, CNG_list, 하이브리드_list, 수소_list, 기타_list]

# fuel_messy_datas를 순회하며 각 연료 타입 리스트에 데이터를 추가합니다.
for i, data in enumerate(fuel_messy_datas):
    # 이제 데이터가 깔끔하게 정렬되었으므로, 나머지 연산자(%)만으로 간단하게 인덱스를 지정할 수 있습니다.
    idx = i % len(pattern_list_2)
    pattern_list_2[idx].append(data)

# 결과를 확인합니다.
print("--- 소계 리스트 ---")
print(소계_list)
print("\n--- 휘발유 리스트 ---")
print(휘발유_list)