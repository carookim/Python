# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 언어 : 파이썬 / 레벨 : 1 /정답률 : 86% 
# 가운데 글자 가져오기

# def solution(s):
# 	return s[len(s)//2]

def solution(s):
	if len(s) % 2 == 0: # 문자열 s의 크기가 짝수라면,
		return s[len(s)//2+1]+s[len(s)//2]
	else: # 문자열 s의 크기가 홀수라면,
		return s[len(s)//2]