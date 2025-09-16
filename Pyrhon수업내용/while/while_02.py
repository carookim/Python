import time

count = 0 
while True:
    print(f'{count}초')
    time.sleep(1) # 1초 지연

    # 5초 단위로 사용자한테  계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count >= 5 and count % 5 == 0:
        answer = input('To be Continue (Y/y) :')
        if answer is 'Y':
            pass
        elif answer is 'y':
            break
        else:
            print("다시 입력해주세요")
            answer = input('To be Continue (Y/y) :')
    else:
        pass
    count += 1

# 자기가 의도한거랑 다르게, 작동하는 걸 버그라고 한다.

#  .upper() ^

count = 0
while True:    
    count += 1
    print(f'{count}초') # 출력
    time.sleep(1)   # 1초간 지연
    
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        is_continue =  input('To be Continue(Y/y)')
        is_continue = is_continue.upper()
        if not is_continue == 'Y':
        # if is_continue == 'Y' or is_continue == 'y':
            break
