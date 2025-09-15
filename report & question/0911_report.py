# 딕셔너리
    # .items()  .keys()  .values()
dict_1 = {
    '001' : '철수',
    '002' : '민수',
    '003' : '준수'
}
print(dict_1)
# 정렬 .items()를 사용하여 정렬,
    # sorted()
print(dict(sorted(dict_1.items(),key = lambda data: data[1])))
# dict_1.items()가 튜플 형태로 나오고 그거중에 value값에 접근하기위해서 data[1]로 입력
print(dict(sorted(dict_1.items(),key = lambda data: data[1]),reversed=True))
# max()
    # max()
# enumerate()
    # 순환문에서 리스트를 감싸면 (인덱스,리스트의값)
# zip()
    # 여러개의 iterable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과','배')
    # [ (1,'사과'), (2,'배')  ]
# map()
    # iterable한 객체의 각 요소에 특정 함수를 적용
    # map(int, ['1','2'])  -> [1,2]

import collections
datas = [1,1,1,1,2,1,3,4,1,2,4,1]
print(collections.Counter(datas))

# Counter() ^
# 아이템의 개수를 세주는 딕셔너리 같은 객체예요. ? ^