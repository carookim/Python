# pip install SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pymysql
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv(".env")

# 2. 환경 변수 확인
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')




# 1. 엑셀 파일 읽기
file_path = "data/자동차등록현황보고_자동차등록대수현황 시도별 (201501 ~ 201812).xlsx"

# 헤더 없이 처음부터 읽기
df = pd.read_excel(file_path,header=0)




# 컬럼 이름 직접 지정 (원하는 이름으로)
df.columns = ['ym', 'region', 'passenger_total', 'bus_total', 'truck_total', 'special_total', 'total_count']

# 필요한 열만 선택 (이미 지정했으므로 생략 가능)
df = df[['ym', 'region', 'passenger_total', 'bus_total', 'truck_total', 'special_total', 'total_count']]

print(df)  # 데이터 확인





def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database='autoreg_kr',
        charset='utf8mb4'
    )

# 1. SQLAlchemy 엔진 생성
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/autoreg_kr?charset=utf8mb4"
)

# 2. 테이블 이름 지정
table_name = "car_reg_region"

# 3. 데이터프레임을 DB로 저장
df.to_sql(
    name=table_name,
    con=engine,
    if_exists='append',  # 기존 테이블 유지 후 추가
    index=False
)

print("데이터베이스 저장 완료!")