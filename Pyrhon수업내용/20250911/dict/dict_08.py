#  정렬
# 딕셔너리 자체를 정렬하는 법? ^

list_a = [('국어',100), ('영어',95),('수학',88)]
# key는 정렬기준으로 정하는 역할
# 람다에서 매개변수 data는 list_a의 데이터

print(sorted(list_a,key= lambda data:data[1])) # 여기서 사용된 람다 함수에선 아규먼트는 생략되었다.

dict_1 = {'국어':100,'영어':956,'수학':88}
print(dict(sorted(dict_1.items(), key=lambda data : data[1]  )))