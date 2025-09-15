# 사용자로부터 점수를 입력받아서 A B C D F 학점을 출력
score = int(input('총점을 입력하세요 :'))
print(f'score = {score}')

if score >= 90:
    # 90 ~ 100
    print('A')
elif score >= 80:
    # 80 ~ 89
    print('B')
elif score >= 70:
    # 70 ~ 79
    print('C')
elif score >= 60:
    # 60 ~ 69
    print('D')
else:
    # ~ 59
    print('F')