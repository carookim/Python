# 이거 만든 이유 ^ 함수 옮길려고

# 함수 모듈

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

def get_data(start, end, input_str = ""):
    while True:
        try:
            input_int = int(input(f'{input_str}({start}~{end}) :'))
            if not start <= input_int <= end:
                raise ValueError(f'{start}~{end} 범위 초과') # ^
            return input_int
        except ValueError as e:
            print(f'오류 : {e}')