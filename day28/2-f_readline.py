# 파일 열기

f = open("c:/pyfile/season.txt")
# season = f.read()
# print(season)
count = 0                           # 전역 변수
while True:
    line = f.readline()             # 한줄씩
    if not line:                    # line이 없으면 멈춤
        break
    count += 1
    print(line, end='')             # 기본적으로 한줄 떨어져서 나옴

print(count)

f.close()