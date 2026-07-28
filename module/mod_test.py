# from 모듈_이름 import 모듈_함수1, 모듈_함수2
from mod1 import add, sub
import mod2
# 전체 다 부르고 싶을때
# from mod1 import * 이런식 or import mod1
if __name__ == "__main__":
    # 모듈1 테스트
    print(add(3 ,4))

    # 모듈2 테스트
    print(mod2.PI)
    a = mod2.Math()
    print(a.solv(2))

"""
sys.path.append("C:/doit/mymod") 이런식으로 추가해서 사용 가능 디렉토리 이동 없이
"""