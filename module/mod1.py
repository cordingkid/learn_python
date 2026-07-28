def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(10, 20))

"""
if __name__ == "__main__":의 의미

위에 없이
print(add(10, 20)) 이렇게 하면 해당 모듈을 불렀을때
저 내용이 실행된다
그래서 그걸 방지 하기 위해 __name__ == "__main__" 이걸 사용한다고 생각하면된다. 관례같은거
"""