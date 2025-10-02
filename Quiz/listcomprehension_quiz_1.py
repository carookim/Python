# 이 활동에서의 목표,
# 한번에 리스트 컴프리헨션으로 작성할 수 있다. 가 목표

# 문제 1: 이름에서 성 추출
# 다음 full_names 리스트에서 각 사람의 성(첫 단어)만 뽑아 새로운 리스트를 만들어보세요.
full_names = ["Kim Ji-eun", "Lee Min-ho", "Park Seo-joon"]

# # 여기에 리스트 컴프리헨션을 작성하세요
# last_names = [  ...  ]

# for문
# last_names = []
# for i in range(0,len(full_names)):
#     full_names[i] = full_names[i].split(' ')
#     last_names.append(full_names[i][0])
# print(last_names)

# 리스트 컴프리헨션으로 for 문을 변환
last_names = [full_names[i].split()[0] for i in range(0,len(full_names))]
# last_names = [name.split()[0] for name in full_names]

print(last_names)

# 문제 2: 문장 첫 단어 추출
# 아래 sentences 리스트에서 각 문장의 첫 번째 단어만 뽑아 새로운 리스트를 만들어보세요.
sentences = ["Hello world", "Python is fun", "OpenAI develops AI"]

# # 여기에 리스트 컴프리헨션을 작성하세요
# first_words = [  ...  ]

# for문
# first_words = []
# for sentence in sentences:
#     first_words.append(sentence.split(' ')[0])
# print(first_words)

# 리스트 컴프리헨션
first_words = [sentence.split(' ')[0] for sentence in sentences]
print(first_words)



# 문제 3: 좌표 리스트에서 x값 추출
# 다음 좌표 리스트에서 각 좌표의 x값(첫 번째 값)만 뽑아 새로운 리스트를 만들어보세요.
points = [(2, 3), (5, 7), (1, 9)]

# # 여기에 리스트 컴프리헨션을 작성하세요
# x_values = [  ...  ]

# for문
# x_values=[]
# for point in points:
#     x_values.append(point[0])
# print(x_values)

# 리스트 컴프리헨션
x_values = [point[0] for point in points]
print(x_values)