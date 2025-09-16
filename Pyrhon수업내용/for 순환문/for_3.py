# remove
list_a = [1,2,1,2]
list_a.remove(1)
print(list_a)

# 1.solution
# list_a에서 1을 지우기 1트
list_a = [1,1,1,2]
index = -1
for i in list_a:
    index += 1
    if i == 1:
        del list_a[index]
print(list_a)
# 앞의 숫자가 지워지면서 인덱스 숫자가 밀림, 그래서 안지워지는 현상이 발생
# 그걸 해결하기위해서 뒤에서부터 지워가는 방식을 채택

list_a = [1,1,1,2]
for i in range(len(list_a)):
    pass

# list_a에서 1을 지우기 2트
# list_a = [1,1,1,2]
# for i in range(5,-1,-1): # [5,4,3,2,1,0] 리스트를 제시
#     if list_a[i] == 1:
#         del list_a[i]
# print(list_a)

#    if list_a[i] == 1:
#        ~~~~~~^^^
# IndexError: list index out of range
# 인덱스 숫자에 맞게 조정, -> 임의의 숫자가 아닌 len(list_a)-1로

# list_a에서 1을 지우기 3트
list_a = [1,1,1,2]
for i in range(len(list_a)-1,-1,-1):
    if list_a[i] == 1:
        del list_a[i]
print(list_a)

# 특정 값을 구분하고 보관하는 방법 ^&

# 1)
# 원본 값을 건드리는 방향보다는 그 값들을 따로 모아두는 방향
# 그리고 그 모아둔 값들을 빈 리스트에 부여하기

# 2)
# 그때 그때 필요없는 값을 수정하여 진행, 되돌리기는 불가, 메모리 효율은 올라갈것으로 기대

# remove() 괄호안의 값과 동일한 첫값을 제거한다.
list_a = [1,1,1,2]
for i in range(len(list_a)):
    if 1 in list_a:
        list_a.remove(1)
print(list_a)

list_a = [1,1,1,2,2,2,2,2,2]
for i in range(len(list_a)): # [9,8,7,6,5,4,3,2,1] 리스트를 제시
    print('*') # 반복된 횟수 확인용
    if 1 in list_a:
        list_a.remove(1) # 처음 나오는 1 제거
    else:
        print(list_a)
        break