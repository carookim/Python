# mysql, python, streamlt 세가지 프로그램을 연동해서  streamlit 사이트 만들기


from dotenv import load_dotenv
import os

# import 프로그램 : pymysql, streamli
import pymysql as ps
import streamlit as st

# import 파일 : shopv2.py
import shopv2

# 사이트 제목
st.title('회원정보 조회 사이트')

# 사이트 메뉴판
st.sidebar.selectbox()