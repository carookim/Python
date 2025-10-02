# 문제 1: 이름에서 성 추출

# 다음 full_names 리스트에서 각 사람의 성(첫 단어)만 뽑아 새로운 리스트를 만들어보세요.

full_names = ["Kim Ji-eun", "Lee Min-ho", "Park Seo-joon"]

# # 여기에 리스트 컴프리헨션을 작성하세요
# last_names = [  ...  ]
for i in range(0,len(full_names)):
    full_names[i] = full_names[i].text.split(' ')
print(full_names)


# 문제 2: 문장 첫 단어 추출

# 아래 sentences 리스트에서 각 문장의 첫 번째 단어만 뽑아 새로운 리스트를 만들어보세요.

# sentences = ["Hello world", "Python is fun", "OpenAI develops AI"]

# # 여기에 리스트 컴프리헨션을 작성하세요
# first_words = [  ...  ]




# 문제 3: 좌표 리스트에서 x값 추출

# 다음 좌표 리스트에서 각 좌표의 x값(첫 번째 값)만 뽑아 새로운 리스트를 만들어보세요.

# points = [(2, 3), (5, 7), (1, 9)]

# # 여기에 리스트 컴프리헨션을 작성하세요
# x_values = [  ...  ]