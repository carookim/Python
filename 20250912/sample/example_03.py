# 숫자 맞추기 게임

# 만든 함수 가져오기
# def get_data(start, end, input_str = ""):
#     while True:
#         try:
#             input_int = int(input(f'{input_str}({start}~{end}) :'))
#             if not start <= input_int <= end:
#                 raise ValueError(f'{start}~{end} 범위 초과') # ^
#             return input_int
#         except ValueError as e:
#             print(f'오류 : {e}')

# 랜덤정수 - 컴퓨터가 선택한 값
# import random as rd # ^

# start, end = 1, 100 # ^
# computer = rd.randint(1,100)
# human = get_data(start,end)

# 게임 로직
# human > computer 크다
# human > computer 작다

# 게임 제작(1)
# if human > computer:
#     print('크다')
# elif human < computer:
#     print('작다')
# else:
#     print('정답')

# 게임제작(2)
# import random as rd # ^

# start, end = 1, 100 # ^
# computer = rd.randint(1,100)

# count = 0
# game_history = []
# is_continue = True
# while is_continue: #
#     count += 1
#     human = get_data(start,end,'입력')
#     if human > computer: #
#         print('작다')
#         game_history.append( (human,'작다' )  )
#     elif human < computer:
#         print('크다')
#         game_history.append( (human,'크다' )  )
#     else:
#         print(f'정답 횟수 : {count}')
#         for guess_value, state in game_history:
#             print(f'{guess_value} - {state}')
#         is_continue = False

# 게임제작(3) : 함수로 만들기(추상화 (Abstraction))

def get_data(start, end, input_str = ""):
    while True:
        try:
            input_int = int(input(f'{input_str}({start}~{end}) :'))
            if not start <= input_int <= end:
                raise ValueError(f'{start}~{end} 범위 초과') # ^
            return input_int
        except ValueError as e:
            print(f'오류 : {e}')

def check_winner(human, computer,game_history, count):
    if human > computer:
        print('작다')
        game_history.append( (human,'작다' )  )
    elif human < computer:
        print('크다')
        game_history.append( (human,'크다' )  )
    else:
        print(f'정답 횟수 : {count}')
        for guess_value, state in game_history:
            print(f'{guess_value} - {state}')
        return True # 적지 않아도 된다. 파이톤에서 None은 True 라고 한다. ^
    return False

import games_utils as gu # ^
import random as rd # ^

start, end = 1, 100 # ^
computer = rd.randint(1,100)

count = 0
game_history = []
while True: # 반복
    count += 1
    human = get_data(start,end,'입력')
    # 승자선택 로직
    if check_winner(human, computer, game_history, count):
        break