# exxcept 오류종류 as e
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
except ValueError as e:
    print(f'오류발생 : ValueError: {e}')
except ZeroDivisionError as e:
    print(f'오류발생 : ZeroDivisionError: {e}')
except IndexError as e:
    print(f'오류발생 : {e.__class__.__name__} : {e}') # ^ e가 어떤종류의 에러인지 알고싶다. -> e.__class__
                                                      # ^ str()이나 그런걸로 <class 'IndexError'>를 IndexError로 바꾸기 -> .__name__
except Exception as e:
    print(f'그밖의 에러 : Exception: {e}')

# if 와 elif 같은 느낌