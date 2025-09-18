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
def create_customer_data():
    sql = 'insert into customer values(null,%s)'
    conn.commit
# 고객정보 업데이트
def update_customer_data():

# 고객정보 조회
def read_customer_data():

# 고객정보 삭제
def delete_customer_data():

# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품명 구매회수 평균구매액

# 4. 기능구현과 테스트가 되면.. streamlit으로 UI 구성 - 템플릿화면을 보고 유사한 형태로 구현

# conn.close() # 접속해제