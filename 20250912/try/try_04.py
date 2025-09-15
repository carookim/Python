# raise 예외 발생하기
try: # 임의로 ValueError를 발생시킨다.
    print("정상코드")
    print("예외 발생")
    # raise "내가 발생시킨 오류"
    # 에러를 발생시키는 키워드 ^ 키워드가 뭔지
    # raise 예외클래스(옵션메시지)
    # raise ValueError("테스트") -> 에러를 일으키는 키워드이지만, 이걸로 에러명을 정할 수 있다. ^ raise의 용도 ^ 시스템에서 인식하는 에러말고도,
                                                                                                # 우리가정한 규칙에서 벗어났을때 에러를 뜨도록 한다.
except Exception as e: # ValueError를 인식하고 에러종류를 출력한다.
    print(f'에러 :{e.__class__.__name__}: {e}')