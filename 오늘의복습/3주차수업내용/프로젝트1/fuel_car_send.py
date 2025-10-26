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

# 시점 -> 시작 지점 -> 2015.01 -> 2025.12

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

# 열로 저장, zip()으로 리스트들의 동일한 인덱스끼리 튜플로 묶기
list_subtotal = list_subtotal[1:] # 계 소계로 되어있어서 인덱스 하나가 밀린다. 그래서 인덱스 1부터 시작하게 한다.
fuel_messy_datas = list(zip(list_subtotal,list_passenger,list_bus,list_truck,list_special))
# print(fuel_messy_datas)
# print(list_subtotal)

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
pattern_list_2_1 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,기타_list]
# print(fuel_messy_datas)

# 1
# for i, data in enumerate(fuel_messy_datas):
#     if i == 0:
#         차종별_list.append(fuel_messy_datas[i])
#     elif i < 982: # 2024.12 부터 2015.11 까지 수소 존재, 2015.10 부터 수소 없음
#         idx = (i - 1) % len(pattern_list_2) # 기존 인덱스 에서 1을 빼고 , 9로 나눈 나머지를 idx로 사용
#         pattern_list_2[idx].append(data)
# # len(fuel_messy_datas), 튜플 갯수 : 1070
# # 2015.10부터 수소가 생성, 그 이후 튜플 갯수 : 88
#     else:
#         idx = (i - 1) % len(pattern_list_2_1) # 기존 인덱스 에서 1을 빼고 , 8로 나눈 나머지를 idx로 사용
#         pattern_list_2_1[idx].append(data)

# 2
# for i, data in enumerate(fuel_messy_datas):
#     if i == 0:
#         # 첫 번째 항목은 차종별
#         차종별_list.append(data)
#     else:
#         # i < 982: 수소 없음 → 8개 패턴
#         # i >= 982: 수소 있음 → 9개 패턴
#         current_pattern = pattern_list_2 if i >= 982 else pattern_list_2_1
#         idx = (i - 1) % len(current_pattern)
#         current_pattern[idx].append(data)


# 3
# pattern_idx = 0  # 패턴 리스트 안에서 어느 리스트에 넣을지 순서를 기억
# for i, data in enumerate(fuel_messy_datas):
#     if i == 0:
#         차종별_list.append(data)
#     else:
#         current_pattern = pattern_list_2 if i >= 982 else pattern_list_2_1
#         current_pattern[pattern_idx].append(data)  # 현재 인덱스에 넣기
#         pattern_idx += 1                          # 다음 리스트로 이동
#         if pattern_idx >= len(current_pattern):
#             pattern_idx = 0                       # 마지막이면 다시 처음으로

# 4
# pattern_list_2 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]
# pattern_list_2_1 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,기타_list]
pattern_idx = 0
for i, data in enumerate(fuel_messy_datas):
    if i == 0:
        차종별_list.append(data)
    elif i < 982:
        idx = (i - 1) % len(pattern_list_2) # 기존 인덱스 에서 1을 빼고 , 9로 나눈 나머지를 idx로 사용
        pattern_list_2[idx].append(data)
    else:
                # 이후 구간: 수소 있음 → 9개 패턴
        current_pattern = pattern_list_2_1
        current_pattern[pattern_idx].append(data)
        
        # 인덱스 순서대로 증가, 끝이면 0으로
        pattern_idx += 1
        if pattern_idx >= len(current_pattern):
            pattern_idx = 0

# print(차종별_list)
# print(휘발유_list)
# print(소계_list)
# 소계 리스트는 2015 초반 구간에 수소항목이 사라져있어서 수정 필요 < - 이거 하는 중 2015.10부터 수소가 생성됨
pattern_list_3 = [소계_list,휘발유_list,경유_list,LPG_list,전기_list,CNG_list,하이브리드_list,수소_list,기타_list]

# 만들어진 리스트 연월별 데이터로 묶기
fuel_types = ['소계','휘발유','경유','LPG','전기','CNG','하이브리드','수소','기타']
insert_data = []

# 연월 리스트 (2015-01 ~ 2024-12)
dates = []
for year in range(2015, 2025):
    for month in range(12, 0, -1):
        dates.append(f"{year}{month:02d}")

# ym별로 차종과 fuel_types 연결
for ym_idx, ym in enumerate(dates):
    for car_idx, 차종_tuple in enumerate(차종별_list):
        car_type = 차종_tuple[0]  # 예: '승용차'

        # 각 fuel_type별 값 추출
        for ft_idx, fuel_type in enumerate(fuel_types):
            # pattern_list_3[ft_idx][car_idx + ym_idx*len(차종별_list)]
            # 안전하게 인덱스 처리
            try:
                value = pattern_list_3[ft_idx][ym_idx * len(차종별_list) + car_idx][ft_idx + 1]
                count = int(value.replace(',', ''))  # '-'는 이미 '0'으로 처리
            except IndexError:
                count = 0
            insert_data.append((ym, car_type, fuel_type, count))


for i in range(0,1071):
    print(insert_data[i])

# sql에 입력을 할때 ym, car_type, fuel_type, car_count