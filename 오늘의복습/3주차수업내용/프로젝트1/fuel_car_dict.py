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

# 시작 지점 클릭
start_point_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]')
start_point_click.click()
time.sleep(2)

# 2015.12 클릭
y2020_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]/option[109]')
y2020_m01_click.click()
time.sleep(2)

# # 2015.01 클릭
# y2015_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]/option[120]')
# y2015_m01_click.click()
# time.sleep(2)

# 2024.12 클릭
y2020_m01_click = driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[2]/option[1]')
y2020_m01_click.click()
time.sleep(2)

# 조회 v 클릭
y2025_m01_click = driver.find_element(By.XPATH,'//*[@id="tabTimeText"]/button[2]')
y2025_m01_click.click()
time.sleep(10)

# 해당 정보를 담은 문자열 추출 (1) X
# soup = BeautifulSoup(driver.page_source,'html.parser')
# fuel_car_datas = soup.select('#mainTable > tbody > tr')
# for row in fuel_car_datas:
#     fuel_car_datas = row.select('tr')
#     for i in range(0,5):
#         print(fuel_car_datas[i].text.strip())
#         time.sleep(10)

# # 해당 정보를 담은 문자열 추출 (2) O : 데이터에 저장하기에는 적절하지않게 나온다. 데이터 저장형식 조정이 필요하다.
# soup = BeautifulSoup(driver.page_source,'html.parser')
# fuel_car_datas = soup.select('#mainTable > tbody > tr')
# for idx, row in enumerate(fuel_car_datas):
#     print(f"행 {idx}: {row.text.strip()}")

# 해당 정보를 담은 문자열 추출 (3) X : fuel_car_datas가 문자열이 아니기때문에 split() 메서드를 지원하지않는다.
# 리스트에 한행을 담는다.
# 그리스트에서 동일한 인덱스 끼리 묶어서 튜플형태로 바꾼다.
# list_passenger = []
# list_bus = []
# list_truck = []
# list_special = []
# soup = BeautifulSoup(driver.page_source,'html.parser')
# fuel_car_datas = soup.select('#mainTable > tbody > tr')
# for i in range(0,5):
#     if i == 0:
#         list_passenger = fuel_car_datas.split(' ')
#     elif i == 1:
#         list_bus = fuel_car_datas.split(' ')
#     elif i == 2:
#         list_truck = fuel_car_datas.split(' ')
#     elif i == 3:
#         list_special = fuel_car_datas.split(' ')
# print(list_passenger)
# print(list_bus)
# print(list_truck)
# print(list_special)

# list_passenger = []
# list_bus = []
# list_truck = []
# list_special = []

# 해당 정보를 담은 문자열 추출 (4)
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

# pirnt(list_subtotal)
# print(list_passenger)
# print(list_bus)
# print(list_truck)
# print(list_special)

# 리스트 컴프리헨션으로  '-'를 '0'으로 변경
change_0 = [list_subtotal,list_passenger,list_bus,list_truck,list_special]
list_subtotal = ['0' if x == '-' else x for x in change_0[0]]
list_passenger = ['0' if x == '-' else x for x in change_0[1]]
list_bus = ['0' if x == '-' else x for x in change_0[2]]
list_truck = ['0' if x == '-' else x for x in change_0[3]]
list_special = ['0' if x == '-' else x for x in change_0[4]]

# print(list_subtotal)
# print(list_passenger)
# print(list_bus)
# print(list_truck)
# print(list_special)

# 만든 list들의 인덱스 0 : car_type
# 만든 list들의 인덱스 1 : 소계
# 만든 list들의 인덱스 2 : 휘발유 fuel_type
# 만든 list들의 인덱스 3 : 경유 fuel_type
# 만든 list들의 인덱스 4 : LPG fuel_type
# 만든 list들의 인덱스 5 : 전기 fuel_type
# 만든 list들의 인덱스 6 : CNG fuel_type
# 만든 list들의 인덱스 7 : 하이브리드 fuel_type
# 만든 list들의 인덱스 8 : 수소 fuel_type
# 만든 list들의 인덱스 9 : 기타 fuel_type
# 10단위로 위 열 항목이 반복
# 10단위로 년도와 월이 묶여서 변한다.

# sql에 입력을 할때 ym, car_type, fuel_type, car_count = 3,176,933

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

# i = 0 차종별_list
# i = 1 소계_list &
# i = 2 휘발유_list
# i = 3 경유_list
# i = 4 LPG_list
# i = 5 전기_list
# i = 6 CNG_list
# i = 7 하이브리드_list
# i = 8 수소_list
# i = 9 기타_lit 0
# i = 10 소계_list & 1
# i = 11 휘발유_list 2
# i = 12 경유_list 3 
# i = 13 LPG_list 4
# i = 14 전기_list 5
# i = 15 CNG_list 6
# i = 16 하이브리드_list 7
# i = 17 수소_list 8
# i = 18 기타_lit 0
# i = 19 소계_list & 1


pattern_list_2 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]
for i, data in enumerate(fuel_messy_datas):
    if i == 0:
        차종별_list.append(fuel_messy_datas[i])
    else:
        idx = (i - 1) % len(pattern_list_2) # 기존 인덱스 에서 1을 빼고 , 9로 나눈 나머지를 idx로 사용
        pattern_list_2[idx].append(data)
        
    # elif i == 1  or (i>= 9 and i % 9 == 1):
    #     소계_list.append(fuel_messy_datas[i])
    # elif i == 2  or (i>= 9 and i % 9 == 2):
    #     휘발유_list.append(fuel_messy_datas[i])
    # elif i == 3  or (i>= 9 and i % 9 == 3):
    #     경유_list.append(fuel_messy_datas[i])
    # elif i == 4  or (i>= 9 and i % 9 == 4):
    #     LPG_list.append(fuel_messy_datas[i])
    # elif i == 5  or (i>= 9 and i % 9 == 5):
    #     전기_list.append(fuel_messy_datas[i])
    # elif i == 6  or (i>= 9 and i % 9 == 6):
    #     CNG_list.append(fuel_messy_datas[i])
    # elif i == 7  or (i>= 9 and i % 9 == 7):
    #     하이브리드_list.append(fuel_messy_datas[i])
    # elif i == 8  or (i>= 9 and i % 9 == 8):
    #     수소_list.append(fuel_messy_datas[i])
    # elif i == 9  or (i>= 9 and i % 9 == 0):
    #     기타_list.append(fuel_messy_datas[i])

# print(차종별_list)
# print('---------------------------------------------------------')
# print(소계_list)
# print('---------------------------------------------------------')
# print(휘발유_list)
# print('---------------------------------------------------------')
# print(경유_list)
# print('---------------------------------------------------------')
# print(LPG_list)
# print('---------------------------------------------------------')
# print(전기_list)
# print('---------------------------------------------------------')
# print(CNG_list)
# print('---------------------------------------------------------')
# print(하이브리드_list)
# print('---------------------------------------------------------')
# print(수소_list)
# print('---------------------------------------------------------')
# print(기타_list)

pattern_list_3 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]

# 연월 리스트 만들기 (2015-01 ~ 2024-12)
from datetime import datetime

dates = []
for year in range(2015, 2025):
    for month in range(12, 0, -1):  # 12월부터 1월까지
        dates.append(f"{year}{month:02d}")

# 연월별 데이터 딕셔너리 초기화
ym_dict = {ym: [] for ym in dates}

# 데이터 9개마다 다음 연월로 넘어가서 저장
current_ym_index = 0

for a in range(len(pattern_list_3)):
    for i, item in enumerate(pattern_list_3[a]):
        ym = dates[current_ym_index]
        ym_dict[ym].append(item)

        # 9개마다 다음 연월로 이동
        if (i + 1) % 9 == 0:
            current_ym_index += 1
            if current_ym_index >= len(dates):
                break

# 확인: 앞 3개 연월만
# for ym, items in list(ym_dict.items())[:3]:
#     print(ym, items)

# sql에 입력을 할때 ym, car_type, fuel_type, car_count

print(ym_dict['202412'])