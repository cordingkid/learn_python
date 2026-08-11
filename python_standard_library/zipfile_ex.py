## zipfile
# zipfile은 여러 개의 파일을 zip 형식으로 합치거나 이를 해체할 때 사용하는 모듈이다.
import zipfile
"""
# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해체하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()

# 특정 파일만 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')

파일을 압축하여 묶고 싶은 경우에는 compression, compresslevel 옵션을 사용할 수 있다.

# 압축하여 묶기
with zipfile.ZipFile('mytext.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    (... 생략 ...)
compression에는 4가지 종류가 있다.

ZIP_STORED: 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
ZIP_DEFLATED: 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성이 좋다).
ZIP_BZIP2: bzip2 압축으로 압축률이 높고 속도가 느리다.
ZIP_LZMA: lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다).
compresslevel은 압축 수준을 의미하는 숫자값으로, 1~9를 사용한다. 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도는 가장 느리지만 압축률이 높다.
"""