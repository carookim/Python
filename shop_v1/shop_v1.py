# pip install pymysql mysql을 접속할 수 있는 라이브러리
# pip install dotenv 환경변수 .env를 로드할 수 있는 라이브러리

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
    database = os.getenv('DB_NAME')
)
# 여기에 작성된 비밀번호와 아이디가 git에서 노출되지않도록 하는 법? 
print('접속성공')
conn.close() # 접속해제
# 2. 각 테이블별 CRUD
# C reate
# R ead
# U pdate
# D elete
# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품명 구매회수 평균구매액
# 4. 기능구현과 테스트가 되면.. streamlit으로 UI 구성 - 템플릿화면을 보고 유사한 형태로 구현