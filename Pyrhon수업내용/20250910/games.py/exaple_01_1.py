# 가위 바위 보 게임 (컴퓨터 VS 휴먼)

# 가위 : 1, 바위 : 2, 보 : 3 : 변수 변환
# 규칙 : 컴퓨터가 임의로 숫자를 선택 : random
# 인간이 숫자를 입력 : input
# 승패를 판별하기 : 비교 연산
# 승패를 기록
# 3번마다 계속할지 물어본다 : 순환문, while

# 위 내용을 요구사항 분석이라고 한다.
# 실무에서는 클라이언트에게 요구사항을 전달받는 과정

# 컴퓨터가 랜덤으로 숫자를 추출,선택된 숫자를 가위/바위/보 로 변환
import random

def computer_input() :
    computer_input = random.randint(1,3)
    if computer_input == 1:
        return '가위'
    elif computer_input == 2:
        return '바위'
    else:
        return '보'

# 사용자가 입력값을 받고,입력한 숫자를 가위/바위/보 로 변환
def user_input():
    user_input = int(input('가위(1) 바위(2) 보(3) 중에서 입력하세요 :'))

    if user_input == 1:
        return '가위'
    elif user_input == 2:
        return '바위'
    elif user_input == 3:
        return '보'
    else:
        print('다시 입력해주세요')
        return user_input()

def calcu(sample_list):
    # 승패 연산(사용자 기준)
    user = sample_list[0]
    comp = sample_list[1]
    
        # 비겼을 경우
    if user == comp:
        print('비겼습니다. 다시입력해주세요.')
    # 사용자가 이겼을 경우
    elif (user == '가위' and comp == '보') or \
         (user == '바위' and comp == '가위') or \
         (user == '보' and comp == '바위'):
        print('축하합니다. 사용자님이 이겼습니다.')
    # 컴퓨터가 이겼을 경우
    else:
        print("아깝네요. 컴퓨터가 이겼습니다.")

# 메인 코드
def is_user_continue(): # 계속 게임을 돌려지게하고, 3번마다 계속할지 물어본다
    count = 0
    game = True
    while game :
    # 3번마다 계속할지 물어본다
        count += 1
        u = user_input() # 사용자 입력 받기
        c = computer_input() # 컴퓨터의 랜덤값 받기
        sample_list = [u, c]
        print(f"사용자 : {u}, 컴퓨터 : {c}")
        calcu(sample_list) # 승패 연산(사용자 기준)

        if  count % 3 == 0: #^
            user_input2 =  input('To be Continue(Y/y)').upper() # upper() ^
            if user_input2 != 'Y':
                print('게임을 종료합니다.')
                break
is_user_continue()

# 반환 return 값을 부여하는거 까먹지말기
# 출력 print는 사용자가 그냥 볼수있는 거고 값이 함수에서 반환되는 게 아니다.
# 그래서 함수가 진행이 안된다?

# count >= 3 라는 명령어는 넣지 않아도 된다. count % 3에서 1이들어오면 나머지는 1이지 0이 아니다.

# 특정 규칙을 찾으면 더 쾌적하게 코드를 구성할 수 있다.

# 함수는 잘게 쪼갤수록 알아보기 좋다.

# 함수를 사용하면 원본을 건드리지 않고 조정할 수 있다.

# 더 간단하게 정리해보기. ^