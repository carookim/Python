# 숫자 맞추기 게임 ^^
import streamlit as st
import random

if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(1,100)
# 컴퓨터 숫자 선택
c_num = st.session_state.c_num

# https://chatgpt.com/s/t_68c9225d19448191806e430a50978d7b 5~8 줄 설명

# 숫자 입력 1~100 사이
h_num = st.number_input('숫자 입력',1,100) # ^ 여기서 1, 100을 입력한 이유
# st.number_input(label, min_value=None, max_value=None, value=0, step=1, ...)
# label: 화면에 표시할 텍스트 (여기서는 '숫자 입력')
# min_value: 입력 가능한 최소값
# max_value: 입력 가능한 최대값
# value: 초기값 (기본 0)
# step: 증가/감소 화살표 클릭 시 값 변화량

if st.button('결과 확인'):
    if c_num > h_num:
        st.write('업')
    elif c_num < h_num:
        st.write('다운')
    else:
        st.write('컴퓨터 숫자 : ', c_num)
        st.write('정답')
        st.ballons() # 축하 애니메이션

# 강사님
# import streamlit as st
# import random
# # 컴퓨터 숫자 선택
# if 'c_num' not in st.session_state:
#     st.session_state['c_num'] = random.randint(1,100)
# c_num = st.session_state.c_num
# # 숫자 입력 1~100 사이
# h_num = st.number_input('숫자 입력',1,100)

# if st.button('결과 확인'):    
#     if c_num > h_num:        
#         st.write('다운')
#     elif c_num < h_num:        
#         st.write('업')
#     else:
#         st.write('컴퓨터 숫자:',c_num)
#         st.write('정답')
#         st.balloons()  # 축하 애니메이션