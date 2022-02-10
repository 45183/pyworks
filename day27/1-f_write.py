# 파일 쓰기


# 파일 열기
f = open("c:/pyfile/test.txt", 'w')             # opem('경로', '모드(w - 쓰기 모드))

# 파일 쓰기
f.write("안녕하세요\n")                          # \n 다음줄
f.write("Have a nice day!!\n")


# 파일 닫기
f.close()