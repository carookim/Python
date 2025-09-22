import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()
# shop_base2_tbl
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database= 'shopinfo'
    )
import crawlingcoffee
# 터미널에서 pip install tqdm
import tqdm # ^
for page_num in tqdm.tqdm(range(1,47)):
    datas = crawlingcoffee.get_coffeshop_data(page_num)
    with get_connection() as conn:
        with conn.cursor() as cur:
            for data in datas:# 한번에 많은 내용을 추가하려고하면 오류가 날수도있어서 일부러 항행씩 처리한다. 그리고 어디부분에 오류가 나는 지 확인
                try:
                    sql = 'insert into shop_base2_tbl values(%s,%s,%s,%s,%s)'
                    cur.execute(sql,(data[0],data[1],data[2],data[3],data[4]))
                except pymysql.err.IntegrityError:
                    sql =  '''
                        update shop_base2_tbl
                        set shop_state=%s, shop_addr=%s, shop_phone_number=%s
                        where shop_area=%s and shop_name=%s
                        '''
                    cur.execute(sql,(data[2],data[3],data[4],data[0],data[1]))
                    conn.commit()
                else:
                    conn.commit()