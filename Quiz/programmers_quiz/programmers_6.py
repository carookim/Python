# https://school.programmers.co.kr/learn/courses/30/lessons/12935
# programmers_6.py
# 언어 : 파이썬 / 레벨 : 1 /정답률 : 85% 
# 제일 작은 수 제거하기

# 탭/스페이스 섞임 주의하기

# def solution(arr):
# 	for i in range(0,len(arr)):
# 		answer = arr[:]
#         if answer[i] == min(arr):
# 			del answer[i]
#             return answer
# (화살표->)방식과 (...)방식이 동일하지않아서 생기는 문제
# space 키 와 tab 키로 다르게 들여쓰기 하는 경우 생기는 오류라고 한다.

def solution(arr):
    for i in range(len(arr)): # range 에서 시작지점은 기본값이 0 이라 기재하지않아도 된다.
        answer = arr[:]
        if answer[i] == min(arr):
            del answer[i]
            return answer   # ← 탭/스페이스 통일

print(solution([4,3,2,1]))