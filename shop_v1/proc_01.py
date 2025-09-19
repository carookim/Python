# pip install pymysql # mysql을 접속할 수 있는 라이브러리
# pip install dotenv  # 환경변수 .env(형식상 자주사용되는 파일이름명)를 로드할수 있는 라이브러리

# 데이터베이스 연결
    # 환경 변수 로드
    # os 를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
    # 커낵션 객체의 cursor 객체를 생성
    # 커서객체의 callproc('AddCodeWithTransaction',[,,,,])
import pymysql as py
from dotenv import load_dotenv
import os

# .env 로드
load_dotenv() # .env 파일을 읽어서 환경변수 등록

# 1. DB 연결
conn = py.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database= 'sqldb'
)
print('접속성공')

# 프로시저 호출 1 ^
# py.AddCodeWithTransaction('PROUD','P1001','소보루빵',0,'Y')

# 프로시저 호출 2
# 함수정의를 통한 실행
def ACWT(a,b,c,d,e):
    sql = 'call AddCodeWithTransaction(%s, %s,%s, %s,%s)'
    conn.cursor().execute(sql,(a,b,c,d,e))
    conn.commit()
    conn.cursor().close()
    print('ACWT 실행완료')

ACWT('PROUD','P1001','소보루빵',0,'Y')

# 프로시저 호출 3
# with as문을 사용한 프로시저 호출
# with conn as conn:
#     with conn.cursor() as cursor:
#         cursor.callproc('AddCodeWithTransaction',['PROD','P1001','소보루빵',0,'Y'])
#         for row in cursor.fetchall():
#             print(row)
#     conn.commit()