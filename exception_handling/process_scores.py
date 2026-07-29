students = ["김철수", "이영희", "박민수", "최유진"]

for student in students:
    try:
        with open(f"{student}_성적.txt", "r") as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError as e:
        print(f"{student}의 성적 파일이 없습니다.")
        continue

# 위 코드에서 일부 학생의 성적 파일이 없어도 프로그램이 중단되지 않고 다른 학생 들의 성적을 계속 처리가능
