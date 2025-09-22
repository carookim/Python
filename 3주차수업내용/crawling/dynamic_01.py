# 동적 사이트에서 데이터를 크롤링 하는 방법
# 구글

# pip install selenium webdriver-manager ^
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터 키등을 인렵하기 위해 사용

import time

# 웹드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')
print('브라우저가 성공적으로 열렸습니다.')
time.sleep(3)

# 검색창 요소 찾기(id가 'ipt_keyword_recruit' 인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME,'gLFyf')

# 검색창에 파이썬 입력
search_input.send_keys('파이썬')
time.sleep(3)

# Enter 키 누르기
search_input.send_keys(Keys.ENTER)
# 여기서 명령어를 입력하는 시간이
# 사이트에서의 지연시간보다 빠른 경우를 대비하여 일부러 지연시키는 기능을 넣는다.
#웹사이트는 서버와 통신하면서 로딩하는 시간이 필요해요. (네트워크 속도, 서버 응답 속도, DOM 요소 렌더링 시간 등)
# 그래서 사이트 로딩이 끝나기 전에 다음 명령을 실행하면 오류가 나요.
# 지연, 대기 명령어
time.sleep(5) # 대략 3초정도 페이즈 로드 될때까지 기다린다.
# driver.quit()