# pip install streamlit - 터미널에서 진행
import streamlit as st
st.title('안녕하세요')
st.write('첫번째 앱')

name = st.text_input
st.write(f'안녕하세요 {name}님!!!')