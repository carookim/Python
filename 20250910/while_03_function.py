# 함수작성을 통해, 작성된 코드를 재활용 하는 법

import time

count = 0 # 함수안에서 정의 내릴수 없는 변수
def display_second(count):
    count += 1
    print(f'{count}초') # 출력
    time.sleep(1)   # 1초간 지연
    return count

# 파이썬에서 함수 안에서 변수를 바꾸면, 그건 기본적으로 함수 지역 변수로만 바뀌어요.
# 함수 밖의 count는 영향을 받지 않아요.
# 그래서 함수 밖의 count를 업데이트하려면, 반환값을 받아서 덮어써야 합니다.

def is_user_continue(count):
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        user_input =  input('To be Continue(Y/y)').upper() # upper() ^
        if user_input == 'Y':
            return True
        else:
            return False
    return True

# count = 0
# while True:    
#     count += 1
#     print(f'{count}초') # 출력
#     time.sleep(1)   # 1초간 지연

# 11,12,13 줄을 display_second()로 대체
# 함수내에 정의 내릴수없는 count값을 밖에 정의 count = 0

# 메인 코드
is_continue = True
while is_continue:    
    count = display_second(count) #1간격으로 출력 #여기서 왜 count = 을 하는 지 ^
    is_continue = is_user_continue(count) # 5초 단위로 진행여부 판단.
    
# # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
# if count % 5 == 0:
#     is_continue =  input('To be Continue(Y/y)')
#     is_continue = is_continue.upper()
#     if not is_continue == 'Y':
#     # if is_continue == 'Y' or is_continue == 'y':
#         break

# 32 - 38 줄을 is_user_continue()로 대체

# ! pip install
# import 말고도 어떤 기능을 불러오는 방법?

# 디버깅 하는 방법