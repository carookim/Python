# 저금통
list_a = [100, 500, 10, 500, 100, 50, 500, 10]
# 저금통에 있는 동전의 종류 10, 50, 100, 500

# set
set_a = {1,2,3,1,2,3,1}
print(f'set_a = {set_a}')

# set은 중복을 제거한다.
# set 내부에 리스트와는 달리, 순서가 없다.

set(list_a)
print()
print(type(set(list_a)))
print(set(list_a))
print()
print(type(list_a))
print(list_a)

print()

# set_a[0] # 자료형 set은, 순서가 지원되지 않기 때문에 에러가 난다.

set_2 = {1,2}
# 셋.add(x), 해당 되는 셋에 x값을 추가한다. 순서는 랜덤이다.
set_2.add(3)
print(set_2)
print()

# 셋.remove(x), 해당되는 셋에 포함된 값중에 x 값을 삭제한다.
# 셋은 중복이 안되서 어차피 한개만 있고, 한개만 삭제된다.
# 그래서 셋에서 어떤요소를 삭제할때는 .remove()를 사용한다.
set_2.remove(2)
print(set_2)
print()

# 셋.pop(index), 해당되는 셋에 index 값을 삭제합니다.
# 하지만 셋은 순서가 정해져 있지않아서 어느 값이 삭제될지 알수없다. ^
set_2.pop()

# 셋.update(), ^
set_2.update()
print(set_2)