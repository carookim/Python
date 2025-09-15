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
except Exception as e:
    print(f'오류발생 : {e}')
except ValueError as e:
    print(f'오류발생 : {e}')

# ValueError: invalid literal for int() with base 10: 'asdasd'
# 문자열로 입력하는 에러이다.
# 실제 출력되는 것과 다른 점은 ValueError가 출력되지 않는다.
# 이부분을 보완하고 디테일하게 어느 종류인지 구분하고 싶다면,(실무에선 거의 Exception 사용)
# Exception자리에 ValueError를 적으면 된다.


print('프로그램 종료')