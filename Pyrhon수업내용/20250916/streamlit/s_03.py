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
# 새션을 사용한다는 것은 상태를 유지

import streamlit as st
if 'count' not in st.session_state: # session_state : Streamlit에서 사용자별로 상태를 저장하는 공간
    st.session_state.count = 0      # 딕셔너리(dictionary)처럼 동작하는 객체다. 그래서 대괄호를 사용한다.

if st.button('카운트 증가'):
    st.write('버튼 클릭됨')
    st.session_state['count'] += 1 # ^여기서 왜 대괄호 인지
st.write('현재 카운트:',st.session_state['count'])
st.json(st.session_state)  # 세션 상태 확인 # ^ json :Python 객체를 JSON 형태로 브라우저에 예쁘게 보여주는 Streamlit 함수예요.
                                            # JSON = JavaScript Object Notation
                                            # 쉽게 말하면 데이터를 텍스트 형식으로 구조화해서 보여주는 표준 포맷