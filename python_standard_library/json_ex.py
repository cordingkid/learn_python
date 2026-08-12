## json
# json은 JSON 데이터를 쉽게 처리하고자 사용하는 모듈이다.
import json
with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data)

data = {'name': '홍길동', 'birth': '0525', 'age': 30}
with open('myinfo.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False) # 한글이 아스키 형태문자열로 변경되는것 방지
