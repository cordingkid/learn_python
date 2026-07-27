"""
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

파일을 열면(open) 항상 닫아(close) 주어야 한다.
이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with 문이 바로 이런 역할을 해 준다. 
다음 예는 with 문을 사용해서 위 예제를 다시 작성한 모습이다.
"""
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
    conent = "Hello"
    print(f.closed) # False (열려있음)
print(f.closed) # True (닫혀있음)
print(conent)

# with문을 사용하면 with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 닫힘
# with문 안에서 만든 변수는 with 문 밖에서도 사용 가능

"""
파일 처리 시 주의 사항

# 한글 파일 쓰기
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
"""