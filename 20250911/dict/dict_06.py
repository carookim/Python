# 딕셔너리의 정실을 이용한 리스트의 요소를 카운트
# max()를 이요해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 키
# 메소드.get() 사용

# 키를 이용해서 값을 가져오는 방법
dict_1 = {'사과' : 10, '포도' : 20}
# 포도의 값
print(dict_1['포도']) # 인덱스 방식 : key값 입력, 없으면 keyerror을 반환
print(dict_1.get('포도')) # 매소드 방식, 없으면 None을 반환
print(dict_1.get('파인애플',0)) # 없으면 0을 반환

# 자료구조에서 가장 큰 값을 찾는 내장함수
print(max([1,45,2,6,7,3,7,457,898]))
# 딕셔너리 자료형이 max에 들어가면, 키 값을 기준으로 계산이된다.
# 숫자가아닌 문자인경우에는
dict_1 = {'국어' : 80, '영어' : 100}
print(max(dict_1))
# 알파벳 순서, 가나다라 순서로 뒤로갈수록 값이 높은 걸로 쳐서
# 출력값이 dict_1의 키값인 '영어'가 나온다.

# (function) def max(
#     iterable: Iterable[SupportsRichComparisonT@max],
#     /, ^
#     *, ^
#     key: None = None ^
# ) -> SupportsRichComparisonT@max

# max(arg1, arg2, *args, *[, key=func]) -> value ^
# ^ 위저것들이 뭔지 알아보기

# 정렬
list_1 = [5,2,1,3]
dict_1.sort # 오름차순으로 정리한다. 작은 수부터 점점 커지는 식으로,
print(sorted(list_1))
# (function) def sorted(
    # iterable: Iterable[SupportsRichComparisonT@sorted],
    # /,
    # *,
    # key: None = None,
    # reverse: bool = False
# 내림차순으로 정렬하는 방법
print(sorted(list_1,reverse = True))
print(sorted(list_1)[::-1]) # ^

# dict
dict_1 = {'국어':80, '국사':100, '영어':98, '수학':88}
print(sorted(dict_1))
print(sorted(dict_1, key = dict_1.get)) # key = dict_1.get :
                                      # key값이 default로 구분하는 기준인데 그걸 임의로 dict_1내부에 있는 value로 설정
                                      # .get 메소드 ^ 딕셔너리에서 안전하게 키값을 통해 값을 가져오는 명령어