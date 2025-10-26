# 공공데이터 자동차 정보조회 관련
# ^ 데이터 관리가 안된건지 조회가 안된다.

from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_KEY')
print(f'P_KEY : {P_KEY[-10:]}')

# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'serviceKey' : P_KEY,
    'registYy' : 2017,
    'registMt' : 11,
    'vhctyAsortCode' : 1,
    'registGrcCode' : 1,
    'useFuelCode' : 2,
    'cnmCode' : '000004',
    'prposSeNm' : 1,
    'sexdstn' : '남자',
    'agrde' : 3,
    'dsplvlCode' : 2,
    'hmmdImpSeNm' : '국산',
    'prye' : 2010,
}

# 데이터를 요청 할 주소
url = f"http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService?serviceKey={P_KEY}"

response = requests.get(url, params=from_data)
print(response.text[:1000])