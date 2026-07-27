## 파일 객체를 for 문과 함께 사용하기
f = open("새파일.txt", 'r')
for line in f:
    print(line)
f.close()
"""
파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.
"""