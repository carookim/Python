# 강사님 작성
# 데이터베이스 연결
    # 환경변수 로드
    # os를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
    # 커넥션 객체의 cursor 객체를 생성
    # 커서객체의 callproc('AddCodeWithTransaction', [, , , ,] )

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 연결통로 생성
conn = pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database='sqldb'
    )
# 보내는 데이터, 명령어 입력 conn.cursor()
with conn.cursor() as cursor:
    cursor.callproc('AddCodeWithTransaction',['ADDR','서울','서울특별시',0,'Y'])
    for row in cursor.fetchall():
        print(row)
conn.commit()
conn.close()    

# 프로시져 호출