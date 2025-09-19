# https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 언어 : 파이썬 / 레벨 : 0 /정답률 : 89% 
# 중복된 숫자 개수

def solution(array, n):
	answer = 0
	for  i  in range(0,len(array)):
		if array[i] == n:
			answer += 1
		else:
			pass
	return answer

list_1 = [1, 1, 2, 3, 4, 5]
print(solution(list_1, 5))


# 모두의 풀이 1
def solution(array, n):
    return array.count(n)

# 모두의 풀이 2
def solution(array, n):
    return sum(1 for x in array if x == n)

# 모두의 풀이 3
def solution(array, n):
    count = 0
    for i in array:
        if i==n :
            count +=1
    return count

# 모두의 풀이 4
def solution(array, n):
    return len([0 for i in array if n == i])

# 모두의 풀이 5
from collections import Counter
def solution(array, n):
    return Counter(array)[n]