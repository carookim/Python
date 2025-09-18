# https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 언어 : 파이썬 / 레벨 : 0 /정답률 : 89% 
# 배열 두배 만들기

def solution(numbers):
	answer = []
	for i in numbers:
		answer.append(i*2)
	return answer

list_1 = [1, 2, 3, 4, 5]
print(solution(list_1))

# 모두의 풀이 1
def solution(numbers):
    return [num*2 for num in numbers]
# 리스트컴프리헨션관련 추가문제 풀기

# 모두의 풀이 2
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))
# map과 람다함수를 사용한 추가문제 풀기

# 모두의 풀이 3
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i]*2)
    return answer

# 모두의 풀이 4
solution = lambda x:[2*y for y in x]

# 모두의 풀이 5
def solution(numbers):
    return [2*i for i in numbers]

# 등등등..
# multiply