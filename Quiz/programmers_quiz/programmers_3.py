# https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 언어 : 파이썬 / 레벨 : 0 /정답률 : 89% 
# 중앙값 구하기


# def solution(array):
# 	sorted(array)
# 	answer = array[len(array)//2]
# 	return answer

# sorted(array) 값을 저장하지않음  수정 -> array = sorted(array)

def solution(array):
	array = sorted(array)
	answer = array[len(array)//2]
	return answer

list_1 = [1, 2, 7, 10, 11]
print(solution(list_1))

# 모두의 풀이 1
def solution(array):
    return sorted(array)[len(array) // 2]