# 1) 파이톤으로 일차적으로 가위바위보 게임 만들기

# 가위바위보 램덤으로 컴퓨터 선정
# import random
# c_number2 = random.randint(1,3)

# 사용자에게서 가위바위보 입력값 받기
# h_input = input("가위 바위 보 중에서 입력하세요 : ")
def get_h_input(h_input_raw):
	if h_input_raw == '가위':
		return 1
	elif h_input_raw == '바위':
		return 2
	elif h_input_raw == '보':
		return 3
	else:
		print('오류 : 다시 입력 해주세요.')
		return None

# 사용자 기준 승리 조건
# 1 3
# 2 1
# 3 2


# 비교 연산 if 조건 문 사용
def yunsan_result(h_input,c_number2):
	'''
	yunsan_result() = None : 무승부
	yunsan_result() = True : 승리
	yunsan_result() = False : 패배
	'''
	if h_input == c_number2:
		return None
	elif (h_input == 1 and c_number2 == 3) \
		or (h_input == 2 and c_number2 == 1) \
		or (h_input == 3 and c_number2 == 2):
		return True
	else:
		return False
	
def result_print(h_input,c_number2):
	if yunsan_result(h_input,c_number2) == None:
		print('무승부입니다.')
	elif yunsan_result(h_input,c_number2) == True:
		print('승리했습니다!')
	elif yunsan_result(h_input,c_number2) == False:
		print('패배했습니다..')

# 계속 실행되게 설정 : 메인코드
import random
while True:
	while True:
		h_input_raw = input("가위 바위 보 중에서 입력하세요 : ")
		h_input = get_h_input(h_input_raw)
		if h_input != None:
			break
	c_number2 = random.randint(1,3)
	yunsan_result(h_input,c_number2)
	result_print(h_input,c_number2)