from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_DECODE_KEY')
print(f'P_KEY : {P_KEY[-10:]}')

# 데이터를 요청 할 주소
url = f"http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService?serviceKey={P_KEY}"

# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'serviceKey' : P_KEY,
    'registYy' : 2017,
    'registMt' : 11,
    'vhctyAsortCode' : '',
    'registGrcCode' : 1,
    'useFuelCode' : 1,
    'cnmCode' : '',
    'prposSeNm' : 1,
    'sexdstn' : '남자',
    'agrde' : 3,
    'dsplvlCode' : 2
}
response = requests.post(url,json=from_data)
print(response.text[:500])