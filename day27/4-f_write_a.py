# 파일 쓰기


# 파일 열기
f = open("c:/pyfile/test.txt", 'a')                 #'a' 모드 : 추가모드    / 그냥 w로 사용시 전에 작성한 내용 사라짐

# 파일 쓰기
f.write("學生\n")


# 파일 닫기
f.close()