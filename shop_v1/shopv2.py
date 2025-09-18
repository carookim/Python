# 수강생 작성

# pip install pymysql # mysql을 접속할 수 있는 라이브러리
# pip install dotenv  # 환경변수 .env를 로드할수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
print('접속성공')

# 2. 각 테이블별 
    # C - insert
    # R - select
    # U - update
    # D - delete

# [
#         {"회원아이디": "user01", "회원이름": "홍길동"},
#         {"회원아이디": "user02", "회원이름": "이몽룡"},
#         {"회원아이디": "user03", "회원이름": "성춘향"}
#     ]


# 고객 - customer

# 고객정보 생성
def create_customer_data(name):
    sql = 'insert into customer values(null,%s)'
    conn.cursor().execute(sql,(name))
    conn.commit()
    print('추가완료')

# 고객정보 업데이트
def update_customer_data(name,customer_id):
    sql = 'update customer set name = %s where customer_id = %s'
    conn.cursor().execute(sql,(name,customer_id))
    conn.commit()

# 고객정보 조회
def read_customer_data():
    sql = 'select * from customer'
    conn.cursor().execute(sql)
    conn.commit()
    print('조회완료')

# 고객정보 삭제
def delete_customer_data():
    sql = 'delete from customer order by customer_id desc limit 1'
    conn.cursor().execute(sql)
    conn.commit()
    print('삭제완료')
# 모든 요소가 다 삭제가 되고나서 삭제할게 없더라도, 삭제할게 없다는 오류 문구는 뜨지 않는다.

# 메인 코드
# AI 기능이 함유된 PK값 초기화 하는 법 : 그냥 sql에 직접입력
# 1. 기존 데이터 삭제 ^
# DELETE FROM customer;
# 2. AUTO_INCREMENT 초기값 초기화 ^
# ALTER TABLE customer AUTO_INCREMENT = 1;

# DELETE FROM customer;
# ALTER TABLE customer AUTO_INCREMENT = 1;

# 파이썬 함수 제작 : AI 기능이 함유된 PK값 초기화 하는 함수
def reset_customer_AI():
    sql = 'delete from customer'
    sql = 'alter table customer auto_increment = 1' # sql 명령어를 여러번 작성해도 작동한다.
    conn.cursor().execute(sql)
    conn.commit()
    print('AI 값이 1로 설정되었습니다.')

# reset_customer_AI() # AI 기능이 함유된 PK값 초기화 하는 함수

# for i in range(5):  # 5개의 이순신 행을 생성
#     create_customer_data('이순신')

# update_customer_data('권율',2) # cutomer_id : 2 에 '권율' 추가
# update_customer_data('신사임당',3) # cutomer_id : 3 에'신사임당' 추가
# update_customer_data('김유신',4) # cutomer_id : 4 에'김유신' 추가
# null상태로 추가한다면? ^
# 반대로 추가한다면?
# update_customer_data(4,'둘리') # 오류가 뜬다
# delete_customer_data() # 마지막에 추가한 항목 삭제, 마지막 항목인 custom_id : 5 , name : 이순신이 삭제
# print(read_customer_data()) # customer 데이터 조회