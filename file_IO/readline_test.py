## 파일을 읽는 여러 가지 방법
# readline 함수 이용
f = open("새파일.txt", 'r')
line = f.readline()
print(line) # 한 줄 읽기
f.close()
