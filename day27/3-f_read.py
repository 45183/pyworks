# 파일 읽기
try:
    f = open('c:/pyfile/testㅇ.txt', 'r')         # opem('경로', '모드(r - 읽기 모드))
    text = f.read()
    print(text)

    # f.close()


    f = open('c:/pyfile/number.txt', 'r')         # opem('경로', '모드(r - 읽기 모드))
    data = f.read()
    print(data)

    f.close()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")