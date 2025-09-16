# session 개념 ^^

# 세션 상태 관리

# import streamlit as st
# count = 0
# if st.button('카운트 증가'):
#     count += 1
#     st.write('현재 카운트 : ', count)
# 이렇게만 작성하면 count가 증가하지않는다.
# Streamlit은 버튼 클릭, 입력값 변경 등 사용자 이벤트가 발생할 때마다
# 전체 스크립트를 맨 처음부터 다시 실행합니다.

# Streamlit에서 값을 누적하려면
# 세션 상태(session_state)를 사용해야 해요.
import streamlit as st
import random
# 컴퓨터 숫자 선택
if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(1,100)
# c_num = st.random.session_state.c_num # ^
# st.write('컴퓨터 숫자:',c_num)
# 숫자 입력 1~100 사이
h_num = st.number_input('숫자 입력',1,100)

if st.button('결과 확인'):    
    if c_num > h_num:        
        st.write('다운')
    elif c_num < h_num:        
        st.write('업')
    else:
        st.write('컴퓨터 숫자:',c_num)
        st.write('정답')
        st.balloons()  # 축하 애니메이션
