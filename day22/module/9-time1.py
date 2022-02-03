import time
# time.sleep(초) - 대기시간

'''
# time.time()

print(time.time())  # 1970.1.1 자정 이후 현재까지 초로 반환한 값
print(time.ctime()) # 현재 날짜와 시간 표기

year = round(time.time() / (365 * 24 * 60 * 60))        # 반올림 - round()
day = round(time.time() / (24 * 60 * 60))

print(year)
print(day)
'''
# 수행 시간 측정하기
start = time.time()

for i in range(1, 11):
    print(i)
    time.sleep(1)       # 1초에 하나씩 출력

end = time.time()

# print("수행 시간 : " + str(end - start) + "초")
print("수행 시간 : %.2f초" % (end-start))