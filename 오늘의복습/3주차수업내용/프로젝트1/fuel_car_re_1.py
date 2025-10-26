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

# 시점 -> 시작 지점 -> 2015.01 -> 2024.12

# 시점 클릭
point_click = driver.find_element(By.ID,'tabTimeText')
point_click.click()
time.sleep(2)

# 2015.01 클릭
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
total_rows = []
for i, row in enumerate(fuel_car_datas[:5]): # 상위 5행만 처리 range(0,4)
    tds = row.select('td')
    total_rows.append([td.text.replace('\xa0','') for td in tds])
#     text = row.text.strip()  # 행의 텍스트 추출
#     cells = text.split('\xa0')  # \xa0 기준으로 분리
#     if i == 0:
#         list_subtotal = cells
#     elif i == 1:
#         list_passenger = cells
#     elif i == 2:
#         list_bus = cells
#     elif i == 3:
#         list_truck = cells
#     elif i == 4:
#         list_special = cells
print(len(total_rows)) # 5

###############################################################
start_month = 12
table_name = "fuel_car"

car_types = ['승용차','승합차','화물차','특수차']
fuel_list = ['휘발유','경유','LPG','전기','CNG','하이브리드','수소','기타','소계']

# 쿼리를 담을 리스트
queries = []

for idx, row in enumerate(zip(*[data[2:] for data in total_rows[1:]])):
    month = start_month - (idx // 9)   # 9개 단위로 월 감소
    ym = f"2024{month:02d}"

    fuel = fuel_list[idx % 9]

    for i, car in enumerate(car_types):
        count = row[i]
        try:
            count_int = int(str(count).replace(',',''))
        except:
            count_int = 0

        # 파라미터화된 튜플 형태로 리스트에 담기
        queries.append((ym, car, fuel, count_int))
#################################################
print(queries[:5])


#                                      #idx = 8   17

# # 저장된 데이터 내부에 있는 '-'를 '0'으로 리스트 컴프리헨션으로 변경
# change_0 = [list_subtotal,list_passenger,list_bus,list_truck,list_special]
# list_subtotal = ['0' if x == '-' else x for x in change_0[0]]
# list_passenger = ['0' if x == '-' else x for x in change_0[1]]
# list_bus = ['0' if x == '-' else x for x in change_0[2]]
# list_truck = ['0' if x == '-' else x for x in change_0[3]]
# list_special = ['0' if x == '-' else x for x in change_0[4]]

# # 열로 저장, zip()으로 리스트들의 동일한 인덱스끼리 튜플로 묶기
# list_subtotal = list_subtotal[1:] # 계 소계로 되어있어서 인덱스 하나가 밀린다. 그래서 인덱스 1부터 시작하게 한다.
# fuel_messy_datas = list(zip(list_subtotal,list_passenger,list_bus,list_truck,list_special))
# # print(fuel_messy_datas)
# # print(list_subtotal)

# # 처음 0만 car_type / 소계 - 휘발유 - 전기 - CNG - 하이브리드 - 수소 - 기타
# # 후에는 저렇게 반복하며 소계_list, 휘발유_list ....에 삽입
# 차종별_list = []
# 소계_list = []
# 휘발유_list = []
# 경유_list = []
# LPG_list = []
# 전기_list = []
# CNG_list = []
# 하이브리드_list = []
# 수소_list = []
# 기타_list = []

# # fuel_messy_datas 데이터를 열 종류(patter_list_2)에 맞춰서 항목순 리스트에 추가하기
# # len(fuel_messy_datas) = 1070, 
# # 수소가 2015.12부터 생성된다. 88

# pattern_list_2 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]
# pattern_list_2_1 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,기타_list]

# # 수소 없는 기간에서 수소_list에 빈공간을 채울 튜플
# PLACEHOLDER = (0, '0', '0', '0', '0')

# # 수소 없는 기간 데이터 개수 (2015.01 ~ 2015.11 → 88개월)
# cutoff = 88 * len(pattern_list_2_1)

# for i, data in enumerate(fuel_messy_datas):
#     if i == 0:
#         차종별_list.append(data)
#         continue
    
#     if i <= cutoff:
#         # 수소 없는 기간 → 8개 열 순환
#         idx = (i - 1) % len(pattern_list_2_1)
#         pattern_list_2_1[idx].append(data)
        
#         # 한 바퀴 끝날 때 수소 자리 채워주기
#         if idx == len(pattern_list_2_1) - 1:
#             수소_list.append(PLACEHOLDER)
#     else:
#         # 수소 있는 기간 → 9개 열 순환
#         idx = (i - 1 - cutoff) % len(pattern_list_2)
#         pattern_list_2[idx].append(data)

# 생성된 리스트 검토하기
# print(차종별_list)
# print('----------------------------------------------------------------------------')
# print(소계_list)
# print('----------------------------------------------------------------------------')
# print(휘발유_list)
# print('----------------------------------------------------------------------------')
# print(경유_list)
# print('----------------------------------------------------------------------------')
# print(LPG_list)
# print('----------------------------------------------------------------------------')
# print(전기_list)
# print('----------------------------------------------------------------------------')
# print(CNG_list)
# print('----------------------------------------------------------------------------')
# print(하이브리드_list)
# print('----------------------------------------------------------------------------')
# print(수소_list)
# print('----------------------------------------------------------------------------')
# print(기타_list)

# 발견된 리스트 문제 :
# 소계_list 마지막 튜플에서 휘발유열이 나온다.
# 수소_list 에