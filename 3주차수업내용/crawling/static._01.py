# 정적 사이트에서 데이터를 크롤링 하는 방법
import requests
# 데이터를 요청 할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터 (1페이지를 보여달라는 의미로)
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gungun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)
print(response.text[:500]) # 그대로 하면 출력될 내용이 많아 길이제한을 걸고 실행