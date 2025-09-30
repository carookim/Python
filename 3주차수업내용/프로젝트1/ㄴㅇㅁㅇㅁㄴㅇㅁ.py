# fuel_car_datas ='3,176,933 1,642,787 949,200 220,151 83,868 7,137 263,004 3,261 7,5'
# print(fuel_car_datas.split())

from datetime import datetime, timedelta
start = datetime(2015, 1, 1)   # 시작 시점
end = datetime(2024, 12, 1)    # 끝 시점

pattern_lists2 = []

current = end
while current >= start:
    pattern_lists2.append(current.strftime("%Y%m"))
    # 한 달씩 줄이기
    if current.month == 1:
        current = current.replace(year=current.year - 1, month=12)
    else:
        current = current.replace(month=current.month - 1)

print(pattern_lists2[:10])  # 앞부분 확인
print(len(pattern_lists2))  # 총 개수