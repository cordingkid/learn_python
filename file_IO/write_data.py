## 파일을 쓰기 모드로 열어 내용 쓰기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()