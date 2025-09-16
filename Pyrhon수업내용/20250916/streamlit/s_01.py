# pip install streamlit - 터미널에서 진행
import streamlit as st
st.title('안녕하세요') # 제목
st.header('해더')
st.subheader('서브 해더')
st.write('첫번째 앱') # 내용
st.button('버튼')
st.checkbox('체크박스')
st.radio('레디오박스',('a','b','c'))
st.selectbox('셀렉트박스',(1,2,3,4,5))
st.slider('슬라이더',0,100,50) # 최대 최소 기본값
st.text_input('텍스트상자')
# st.image()
# st.audio()

name = st.text_input('이름')
st.write(f'안녕하세요 {name}님!!!')