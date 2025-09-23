from dotenv import load_dotenv
import os

import requests

# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_KEY')
print(f'P_KEY :{P_KEY[:10]}')

# 데이터를 요청할 주소
url = 'http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService'

# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'servicekey' : P_KEY,
}

response = requests.get(url,data=from_data)
print(response.text[:500])
import json