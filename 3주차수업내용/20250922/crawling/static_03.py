# Data Base접속
# insert 쿼리문을 이용해서 수집한 데이터를 DB에 저장
# DB 에 접속
import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database= 'shopinfo'
    )

import crawlingcoffee
for page_num in range(1,47): # 전체 페이지 조회 설정
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            insert into shop_base_tbl
            values(null,%s,%s,%s,%s,%s);
            '''
            cur.executemany(sql,crawlingcoffee.get_coffeshop_data(page_num))
            # print('데이터 추가 성공')
        conn.commit()