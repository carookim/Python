# 에러 예상
# 두개의 숫자값을 입력하고, 두 값을 사칙연산한 값을 출력한다.

try:
    num1, num2 = map(int, input('공백을 기준으로 두개의 숫자를 입력').split())
    calc_lists = [num1+num2,num1-num2,num1*num2,num1/num2]

    # print(f'{num1} + {num2} = {calc_lists[0]}')
    # print(f'{num1} - {num2} = {calc_lists[1]}')
    # print(f'{num1} x {num2} = {calc_lists[2]}')
    # print(f'{num1} ÷ {num2} = {calc_lists[3]}')

    print('1. 더하기',end='\t')
    print('2. 빼기',end='\t')
    print('3. 곱하기',end='\t')
    print('4. 나누기',end='\t')
    choice = int(input('원하는 결과를 입력하세요 : '))
    print(f'결과는 = {int(calc_lists[choice-1])}')
except:
    print('오류발생')

print('프로그램 종료')

# (3줄)숫자 입력할때 문자열을 입력 ValueError
# 0으로 연산 할때, 나누기에서 ZeroDivisionError
# (15줄)잘못된 선택 숫자를 입력하면 IndexError
# (15줄)인덱스 입력에서 문자열을 입력 ValueError

# try:
#     예외가 발생할 가능성이 있는 코드
# except:
#     예외가 발생했을 때 실행할 코드
# else:
#     예외가 발생하지 않았을 때 실행할 코드
# finally:
#     무조건 실행할 코드

# try와 except가 주로 사용된다.

# 오류가 나든 안 나든, finally 안의 코드는 항상 실행된다.
# 좀 더 설명하자면, finally는 파일 닫기처럼 “꼭 해야 하는 작업”을 안전하게 보장해줘요.

# finally를 실행하기 이전에 try, except, else 등의 단계에서 return을 만났을 경우
# 어떻게 될까?
# 좀더 구체적으로 설명하자면, try에 return이 있으면
# try가 작동되고 finally가 작동된다. 그 중간에 except, else는 작동되지않지만 try자체가 finally는 무조건
# 작동한다 라는 기능이 있어서 finally작동 이전에 return이 쓰여도 작동이 된다.