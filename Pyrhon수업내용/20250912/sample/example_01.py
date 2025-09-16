# 사용자 입력 처리 함수
# 함수명 : get_data()
# 파라미터 명칭 :
    # start : 시작값
    # end : 종료값
    # input_str : 가이드 문구
# return 값 :
    # 정수로 변환된 값

# def get_data():
#     input_str = input('정수를 입력하세요(1~100) :')
#     print(int(input_str))

# 시스템에상에서는 문자열 입력을 에러가 뜨고, 우리가세운 조건(1~100)에서는 에러인 500은 시스템상으로 넘어간다.
# 이부분을 임의로 이조건을 넘었을때 에러가 뜨도록 만들어 볼꺼다.

# def get_data():

# 1)
# while True:
#     try:
#         input_int = int(input('정수를 입력하세요(1~100) :'))
#         if not 0 <= input_str <= 100:
#             raise ValueError('1~100 범위 초과')
#     except: # ^ except Exception as e: 이거는 오류를 출력하거나 알아낼때 사용하는건가?
#         input_str = int(input('정수를 입력하세요(1~100) :'))
#     else:
#         break

# 2) ValueError 예외처리 와 함수로 만들기(추상화 (Abstraction))
# def get_data(start, end, input_str = ""):
#     while True:
#         try:
#             input_int = int(input(f'{input_str}({start}~{end}) :'))
#             if not start <= input_int <= end:
#                 raise ValueError(f'{start}~{end} 범위 초과')
#             else:
#                 print(input_int)
#         except Exception as e:
#             print(f'오류 : {e}')
#         else:
#             break

# get_data(2,100,'정수')

# 3) 좀더 최적화하기 : return 사용 및 코드 간략화하기
# def get_data(start, end, input_str = ""):
#     while True:
#         try:
#             input_int = int(input(f'{input_str}({start}~{end}) :'))
#             if not start <= input_int <= end:
#                 raise ValueError(f'{start}~{end} 범위 초과')
#         except Exception as e:
#             print(f'오류 : {e}')
#         else:
#             return input_int # 여기서 지역변수 input_int가 닿지않는 언어도 있나보다.

# print(get_data(2,100,'정수'))

def get_data(start, end, input_str = ""):
    while True:
        try:
            input_int = int(input(f'{input_str}({start}~{end}) :'))
            if not start <= input_int <= end:
                raise ValueError(f'{start}~{end} 범위 초과') # ^
            return input_int
        except ValueError as e:
            print(f'오류 : {e}')


print(get_data(2,100,'정수'))