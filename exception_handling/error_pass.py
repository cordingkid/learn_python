try:
    # 설정 파일을 읽으려 시도
    with open("설정파일.txt", "r") as f:
        config = f.read()
except FileNotFoundError as e:
    pass # 설정 파일이 없어도 계속 진행

# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")