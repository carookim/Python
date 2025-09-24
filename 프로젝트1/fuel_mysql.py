import pymysql
from dotenv import load_dotenv
import os

# .env 로드
load_dotenv()

# sautoreg_kr
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database= 'autoreg_kr'
    )
conn = get_connection()
cur = conn.cursor()
import fuel_car

# INSERT 쿼리
sql = "INSERT INTO fuel_stats (ym, car_type, fuel_type, car_count) VALUES (%s, %s, %s, %s)"

insert_data = []

for ym, data_list in ym_dict.items():
    for item in data_list:
        car_type = item[0]  # 튜플 첫 번째 요소가 차종

        # item 길이 부족 시 0으로 채우기 (차종 포함 총 10개)
        total_length_needed = len(fuel_types) + 1
        if len(item) < total_length_needed:
            item = tuple(list(item) + ['0'] * (total_length_needed - len(item)))

        # fuel_types별로 car_count 추출
        for ft_idx, fuel_type in enumerate(fuel_types):
            count_str = item[ft_idx + 1]  # +1 : 차종 제외
            count = int(count_str.replace(',', ''))  # 이미 '-'는 '0'으로 처리되어 있음
            insert_data.append((ym, car_type, fuel_type, count))

# MySQL에 한 번에 삽입
try:
    cur.executemany(sql, insert_data)
    conn.commit()
    print(f"총 {len(insert_data)}건 삽입 완료")
except pymysql.err.IntegrityError as e:
    print("무결성 오류 발생:", e)
finally:
    conn.close()