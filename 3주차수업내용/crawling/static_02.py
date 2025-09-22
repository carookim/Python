import requests # ^ 이거 무슨기능을 import한건지
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 연결통로 생성, 이전에 mysql통로생성하는 것과 동일하다!
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gungun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)

# command prompt에
# pip install beautifulsoup4 입력 및 실행
# BeautifulSoup 은 파이썬에서 HTML, XML 문서를 파싱(구조 분석)해서 원하는 데이터를 쉽게 뽑아내는 라이브러리이다.
from bs4 import BeautifulSoup
# response 에 있는 문자열로 된 데이터를 Beautiful 객체로 변환
# Beautiful 앞문자가 대문자인 객체는 클래스명으로, Beautiful 클래스에 속한 객체로 변환하겠다는 말
soup = BeautifulSoup(response.text,'html.parser') # ^ response.text를 괄호안에 넣는 것까지는 알겠는데, 'html.parser'을 뒤에적는 이유

# 원하는 정보를 추출
# f12 로 원하는 부분을 클릭해 복사, 하단 복사종류 나열
# /html/body/div[2]/div[2]/div[1]/div[2]/fieldset/fieldset/div[1]/table/tbody : full path
# //*[@id="contents"]/div[2]/fieldset/fieldset/div[1]/table/tbody : x path
# document.querySelector("#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody") :js path
# #contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody : copy selecter

# copy selecter 참고
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody'
# soup.select('tbody > tr') tbody가 한개 밖에 없어서 가능한 방식이다.
# 만약 여러개면 가장 먼저 만나는 tbody를 조회하게 된다.
store_rows = soup.select(str_table_rows)
print(store_rows[0])
print(soup.select('td')[0].text.strip()) #지역
print(soup.select('td')[1].text.strip()) #매장명
print(soup.select('td')[2].text.strip()) #현황
print(soup.select('td')[3].text.strip()) #주소
# print(soup.select('td')[4].text.strip()) #아이콘이라서 텍스트로 안될꺼라 예상되어 뺏다.
print(soup.select('td')[5].text.strip()) #전화번호
# 첫번째 칸에 있는 정보가 조회되었다.

#세번째 칸 조회해보기 ^

# for idx,row in enumerate(store_rows): # 1페이지 한 행을 출력하는 함수 # idx,row로 받는 이유, enumerate ^ 갯수확인
#     print(idx+1) # ^ 이거 무슨 기능?
#     print(soup.select('td')[0].text.strip()) #지역
#     print(soup.select('td')[1].text.strip()) #매장명
#     print(soup.select('td')[2].text.strip()) #현황
#     print(soup.select('td')[3].text.strip()) #주소
#     print(soup.select('td')[5].text.strip()) #전화번호
#     print('*'*100)

# 수집한 정보를 사용하기위해선 두가지 기능을 만들어야한다.
# 데이터를 조회하고, 그 정보를 저장하는 기능을 만든다.

# 방금 조회하는 방법을 배웠다면ㅡ 이제 이 정보를 저장하기위해 테이블로 변환시키는 과정을 가져볼꺼다.
# 튜플로 변환하고 리스트로 감싸기.

store_lists = []
for row in enumerate(store_rows):
    store_lists.append(
    (
    row.select('td')[0].text.strip(),
    row.select('td')[1].text.strip(),
    row.select('td')[2].text.strip(),
    row.select('td')[3].text.strip(),
    row.select('td')[5].text.strip()
    )
    )


# Data Base접속
# insert 쿼리문을 이용해서 수집한 데이터를 DB에 저장
# DB 에 접속
# 이부분은 static_03.py 이어서