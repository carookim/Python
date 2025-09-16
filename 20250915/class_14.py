# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드 __str__, __eq__, __ne__, __lt__, __gt__, __le__, __ge__
# property, getter, setter, deleter, private -> 함수를 변수처럼 사용 # private를 로직으로 만들기 위해서 사용
# 객체생성

# 상품관리
# 상품명 product_name, 가격 product_price, 재고 product_stock

# 상품 클래스  # 상품명
              # 가격
              # 재고

class Product:
    count = 0 # 클래스 함수 Product클래스인 모든 인스턴스 함수가 접근 가능
    def __init__(self, name, price, stock):
        self.product_name = name
        self.product_price = price
        self._product_stock = stock

    @property
    def product_stock(self):
        return self._product_stock
    
    @product_stock.setter
    def product_stock(self, stock):
        if stock >= 0:
            self._product_stock = stock
        else:
            print('재고는 0보다 작을 수 없습니다.')

    def __str__(self): # print()로 출력할때 자동호출
        return f'상품명 : {self.product_name}, 가격 : {self.product_price}, 재고 : {self.product_stock}'
    
s1 = Product('비비빅',690, 70)
print(s1.product_name)
print(s1.product_price)
print(s1.product_stock) # private 변수지만 proeprty로 접근가능

# .id ^

# --- 강사님 예제 ---

# self._product_stock = value            

# def __str__(self):
#         return f'상품명: {self.product_name}, 가격: {self.product_price}, 재고: {self.product_stock}'
#         return f'상품명: {self.product_name}, 가격: {self.product_price}, 재고: {self.product_stock}'

# products = [
#     Product("노트북", 1000000, 10),
#     Product("스마트폰", 500000, 20),
#     Product("태블릿", 300000, 15)
# ]    
# 노트북의 가격을 20% 인하
# 스마트폰은 가격을 10% 인상

# 숙제 :
# 제품 출력
# 전체제품 출력
# 제품 추가
# 제품 삭제
# 현재 모든 재품의 수량