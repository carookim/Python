# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# programmers_5.py
# 언어 : 파이썬 / 레벨 : 0 /정답률 : 89% 
# 짝수는 없어요

def solution(n):
	answer = []
	for i in range(1,n+1):
		if i%2 == 0: # 짝수인 경우
			pass
		elif i%2 != 0: # 홀수인 경우
			answer.append(i)
		answer.sort()
	return answer

print(solution(15))

# 모두의 풀이 1
def solution(n):
    return [i for i in range(1, n+1, 2)]

# 모두의 풀이 2
def solution(n):
    return [x for x in range(n + 1) if x % 2]

# 모두의풀이 3
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if i % 2 == 1:
            answer.append(i)

    return answer