# pip install pymysql mysql을 접속할 수 있는 라이브러리
# pip install dotenv 환경변수 .env를 로드할 수 있는 라이브러리

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()
# 1. DB 연결 하는 명령어 형식
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
# 여기에 작성된 비밀번호와 아이디가 git에서 노출되지않도록 하는 법? 
print('접속성공')
# conn.close() # 접속해제

# ----------------------

# 2. 각 테이블별 CRUD
    # C reate
    # R ead
    # U pdate
    # D elete
# 고객 - customer
# 고객 생성
def create_customer(name):
    sql = 'insert into customer values(null,%s)' # sql 명령어 작성시 sql = 'sql 명령어'
    cur = conn.cursor() # ^
    cur.execute(sql,name) # ^
    conn.commit() # ^
    print('고객추가 완료')

# 고객 조회
def readAll_customers(isDict = False): # ^
    sql = 'SELECT * FROM customer;'
    if isDict:
        cur = conn.cursor() # ^
        cur.execute(sql) # ^
        for c in cur.fetchall(): # ^
            print(f'{c['customer_id']} {c['name']}')
    else:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(pymysql.cursors.DictCursor)
        for c in cur.fetchall():
            print(f'{c[0]} {c[1]}')
    print('조회완료')

# # ^에 사용된 함수와 용어 개념 https://chatgpt.com/s/t_68cb981b45dc8191ae4c7e77f4cdfda0
# 위 개념의 예제 https://chatgpt.com/s/t_68cb982e742c819184a5d663d9218b78

# 고객정보 업데이트
def update_customer(customer_id, name):
    sql = '''
        update customer
            set name = %s
        where customer_id = %s
    '''
# 여기서 %s의 기능 ^
    with conn.cursor() as cur:
        cur.execute(sql,(customer_id,name))
    conn.commit()

# 위코드를 sql명령어와 비교한 내용
# https://chatgpt.com/s/t_68cb9e03de088191b4497ebbac2a0cc0

# 고객정보 삭제
def delete_customer(customer_id):
    sql = 'delete from customer where customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql,customer_id)
    conn.commit
    print(f'삭제되었습니다. {customer_id}')

create_customer('abc')
readAll_customers()
update_customer(1,'abc')
delete_customer(1)

# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품명 구매회수 평균구매액

# 4. 기능구현과 테스트가 되면.. streamlit으로 UI 구성 - 템플릿화면을 보고 유사한 형태로 구현

conn.close() # 접속해제