# 명령어는 모두 실행이된다.
# 조건문을 이용하면 특정 명령문은 실행되지않게 할 수 있다.
# 흐름제어?

# 조건문은 if 조건:
# 들여쓰기를 해서 if에 하위 명령어로 만든다. -> 블럭

age = 20
if age >= 18:
    print("성인입니다.")
    print("조건문은 True입니다.")
    #
    #
    #
print('if와 상관없는 명령어')
print()

# 조건이 맞으면 합격 그렇지 않으면 불합격
score = 80
if score >= 60:
    print("합격")
else:
    print("불합격")

# 온도별 춥고 더운 정도
temperatur = 25
if temperatur > 30:
    print('덥다')
elif temperatur > 20:
    print('따뜻하다')
# else:
#     if temperatur > 20:
#         print("따뜻하다")
elif temperatur > 10:
    print('시원하다')
else:
    print('춥다')