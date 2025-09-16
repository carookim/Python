# ^
import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="코드로 만든 게임 모음",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("메뉴")
    selected_menu = st.radio(
        "원하시는 메뉴를 선택하세요:",
        ["숫자 맞추기", "가위 바위 보","도움말"]
    )

# 메인 컨텐츠 영역
def show_game():
    st.header("숫자 맞추기")
    st.write("환영합니다! 이곳은 숫자 맞추기 게임 페이지입니다.")
    
    if 'c_number' not in st.session_state: # 딕셔너리 키값 여부 확인
        st.session_state.c_number = random.randint(1,100)
      # st.session_state['c_number'] = random.randint(1,100)

    c_number = st.session_state.c_number
    # number_input 위젯에서 엔터기가 입력되었을 때 값을 리턴해서 h_number에 저장
    h_number  =st.number_input('1에서 100사이의 숫자를 입력하세요 : ',1,100) # ^
    st.write(f'입력한 숫자 : {h_number}')

    if st.button('결과 확인'):    
        if c_number > h_number:        
            st.write('다운')
        elif c_number < h_number:        
            st.write('업')
        else:
            st.write('컴퓨터 숫자:',c_number)
            st.write('정답')
            st.balloons()  # 축하 애니메이션
        # ! 게임 다시실행 코드 + c_number del 로 초기화하기

def show_game2():
    st.header("가위 바위 보")
    st.write("환영합니다! 이곳은 가위 바위 보 게임 페이지입니다.")
    def get_h_input(h_input_raw):
        if h_input_raw == '가위':
            return 1
        elif h_input_raw == '바위':
            return 2
        elif h_input_raw == '보':
            return 3
        else:
            print('오류 : 다시 입력 해주세요.')
            return None
        
    # 비교 연산 if 조건 문 사용
    def yunsan_result(h_input,c_number2):
        '''
        yunsan_result() = None : 무승부
        yunsan_result() = True : 승리
        yunsan_result() = False : 패배
        '''
        if h_input == c_number2:
            st.write('비김')
        elif (h_input == 1 and c_number2 == 3) \
            or (h_input == 2 and c_number2 == 1) \
            or (h_input == 3 and c_number2 == 2):
            st.write('이김')
        else:
            st.write('짐')
        
    

    # 계속 실행되게 설정 : 메인코드
    # 문자열 입력

    h_input_raw = st.text_input('입력하세요 가위 바위 보')
    h_input = get_h_input(h_input_raw)
    
    c_number2 = random.randint(1,3)
    yunsan_result(h_input,c_number2)


def show_help():
    st.header("도움말")
    st.write("도움이 필요하시다면 아래 연락처로 문의해주세요:")
    st.write("이메일: help@example.com")

# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "숫자 맞추기":
    show_game()
elif selected_menu == '가위 바위 보':
    show_game2()
elif selected_menu == "도움말":
    show_help()

# 가위 바위 보 게임을 streamlit 에 구현하기 s_06.2py 참고