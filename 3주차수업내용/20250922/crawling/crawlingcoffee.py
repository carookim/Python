# 모듈로 사용하려면 파일명에 언더바가 들어가면 안된다.
def get_coffeshop_data(page_num):
    import requests # ^ 이거 무슨기능을 import한건지
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
    # 연결통로 생성, 이전에 mysql통로생성하는 것과 동일하다
    from_data = {
        'pageNo' : page_num, # 페이지 번호
        'sido' : '',
        'gungun' : '',
        'store' : ''
    }
    response = requests.post(url,data=from_data)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text,'html.parser')

    # 가져올 정보 경로 지정?
    str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr' # 주소 등록 잘해두기
    store_rows = soup.select(str_table_rows)

    # 지정한 정보를 튜플로 만든다음에 리스트로 요소로 저장
    store_lists = []
    for row in store_rows:
        store_lists.append(
        (
        row.select('td')[0].text.strip(),
        row.select('td')[1].text.strip(),
        row.select('td')[2].text.strip(),
        row.select('td')[3].text.strip(),
        row.select('td')[5].text.strip()
        )
        )
    return store_lists # 값을 리턴하기
