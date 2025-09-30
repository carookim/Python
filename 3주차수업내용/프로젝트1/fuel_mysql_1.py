# ------------------------------
# 1️⃣ 필요 라이브러리
# ------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pymysql
from dotenv import load_dotenv
import os

# ------------------------------
# 2️⃣ 웹 크롤링
# ------------------------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://stat.eseoul.go.kr/statHtml/statHtml.do?orgId=201&tblId=DT_201004_I020004&conn_path=I2&obj_var_id=&up_itm_id=')
driver.maximize_window()
time.sleep(3)

# 시점 클릭
driver.find_element(By.ID,'tabTimeText').click()
time.sleep(2)

# 시작 지점 클릭
driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]').click()
time.sleep(2)

# 2020.01 클릭 (예시)
driver.find_element(By.XPATH,'//*[@id="timeM"]/h2/select[1]/option[120]').click()
time.sleep(2)

# 조회 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="tabTimeText"]/button[2]').click()
time.sleep(10)

# ------------------------------
# 3️⃣ BeautifulSoup로 데이터 추출
# ------------------------------
soup = BeautifulSoup(driver.page_source,'html.parser')
fuel_car_datas = soup.select('#mainTable > tbody > tr')

# 상위 5행만 처리
list_subtotal, list_passenger, list_bus, list_truck, list_special = [], [], [], [], []

for i, row in enumerate(fuel_car_datas[:5]):
    text = row.text.strip()
    cells = text.split('\xa0')
    # '-' → '0'
    cells = ['0' if x == '-' else x for x in cells]
    
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

# ------------------------------
# 4️⃣ subtotal만 int로 변환
# ------------------------------
# 맨 앞 '소계' 문자열 제외
list_subtotal_num = [int(x.replace(',', '')) for x in list_subtotal[1:]]

# ------------------------------
# 5️⃣ 연월 리스트
# ------------------------------
dates = [f"{y}{m:02d}" for y in range(2015, 2025) for m in range(12,0,-1)]

# ------------------------------
# 6️⃣ DB 삽입용 insert_data 생성
# ------------------------------
fuel_types = ['소계','휘발유','경유','LPG','전기','CNG','하이브리드','수소','기타']
차종별_list = [list_passenger, list_bus, list_truck, list_special]
pattern_list_3 = [list_subtotal, list_passenger, list_bus, list_truck, list_special]

insert_data = []

for ym_idx, ym in enumerate(dates):
    for car_idx, 차종 in enumerate(차종별_list):
        car_type = 차종[car_idx]
        for ft_idx, fuel_type in enumerate(fuel_types):
            try:
                if fuel_type == fuel_types[ft_idx]:
                    # subtotal int값 사용
                    value = list_subtotal_num[ym_idx]
                else:
                    # 나머지는 문자열 그대로 (DB 컬럼이 INT라면 필요시 int 변환)
                    value = pattern_list_3[ft_idx][car_idx + 1]  # 첫 번째 차종 이름 제외
                count = int(value.replace(',', '')) if fuel_type == '소계' else value
            except (IndexError, ValueError):
                count = 0
            insert_data.append((ym, car_type, fuel_type, count))

# ------------------------------
# 7️⃣ MySQL에 삽입
# ------------------------------
conn = pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database= 'autoreg_kr'
)
cur = conn.cursor()

sql = "INSERT INTO fuel_cars (ym, car_type, fuel_type, car_count) VALUES (%s, %s, %s, %s)"

try:
    cur.executemany(sql, insert_data)
    conn.commit()
    print(f"총 {len(insert_data)}건 삽입 완료")
except pymysql.err.IntegrityError as e:
    print("무결성 오류 발생:", e)
finally:
    conn.close()
