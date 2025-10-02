# https://school.programmers.co.kr/learn/courses/30/lessons/120823
# 언어 : 파이썬 / 레벨 : 1 /정답률 : 89% 
# 직각삼각형 출력하기

# 문제 설명
# "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다.
# 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

# 제한사항
# 1 ≤ n ≤ 10
# 입출력 예
# 입력 #1
# 3

# 출력 #1
# *
# **
# ***
# 입출력 예 설명
# 입출력 예 #1

# n이 3이므로 첫째 줄에 * 1개, 둘째 줄에 * 2개, 셋째 줄에 * 3개를 출력합니다.

# n이 1씩 뺀다.
# 임의의 값 k가 n을 동일해질때 까지 1씩 더한다.

#입력값 n 을 받는다.
# 임의의 값 k가 n을 동일해질때 까지 1씩 더한다.

# try:
#     n = int(input())
# except ValueError:
#     print("입력값이 정수가 아닙니다.")
# except EOFError:
#     print("입력이 없습니다(EOF). 터미널에서 실행하거나 입력을 제공하세요.")

n = int(input())
for k in range(1,n+1):
    print('*'*k)

# input() 이 작동하지않는 이유

# 다른사람 풀이 1 - join 사용
print('\n'.join('*' * (i + 1) for i in range(int(input()))))

# 다른사람 풀이 2
n = int(input())
for i in range(1,n+1):
    print('*'*i)