# 1 ~ 100
import random

datas = [ random.randint(1,100) for i in range(10) ]
print(datas)

import streamlit as st
st.write('막대 그래프') # ^ st.write도 print()처럼 마지막에 행변환을 하나?
st.bar_chart(datas)

st.write('선 그래프')
st.line_chart(datas)

st.write('영역 그래프')
st.area_chart(datas)

st.write('1x2 layout')
col1, col2 = st.columns(2) # col1 col2가 1x2 layout에 들어갈 이미지 위치명이다.
col1.bar_chart(datas)
col2.line_chart(datas)

st.write('2x2 layout')
col1, col2 = st.columns(2) # col1 col2 col3 col4가 2x2 layout에 들어갈 이미지 위치명이다.
with col1:
    st.write('막대그래프')
    st.bar_chart(datas)
with col2:
    st.write('선그래프')
    st.line_chart(datas)

col3, col4 = st.columns(2)
col1.bar_chart(datas)
col2.line_chart(datas)
col3.area_chart(datas)
col4.table(datas)