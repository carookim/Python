# 중첩 for
for i in range(3): # -> [0,1,2]
    for i in range(3):
        print(i)
        # 가장 안쪽에 있는 i로 접근

for i in range(3): # -> [0,1,2]
    for j in range(3):
        print(f'i : {i} j : {j}')
    print()