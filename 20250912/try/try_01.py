# 오류를 (예방하고_완성하는 단계면 예방 제작하는 과정이면 그때에 따라 다를듯)
# 피해가는 행위 -> 예외 처리

# 숫자를 입력합니다.
number_input_a = int(input("정수 입력> "))
# 정수형으로 변환하는데 숫자가 들어가야한다.
# 작은 공백 하나가 포함되더라도 에러가 뜬다.

# 출력합니다.
print("원의 반지름 : ", number_input_a)
print("원의 둘레 : ", 2*3.14*number_input_a)
print("원의 넓이 : ", 3.14*number_input_a*number_input_a)
print('ㅡ'*30)

# num1 = (input("숫자를 입력하세요 : ")
# num2 = input("숫자를 입력하세요 : ")

# 예외처리하기전,
# 두개의 숫자값을 입력하고, 두 값을 사칙연산한 값을 출력한다.
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

# .isdigit()
# .split()
# .map( , )
# print( , end='\t')
# try
# except 오류종류 as e: -> 발생한 오류 객체를 e라는 변수에 담는다는 뜻이에요.
# raise 구문