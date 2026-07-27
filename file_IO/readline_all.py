# 모든 줄 읽기
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line) # 한 줄 읽기
f.close()