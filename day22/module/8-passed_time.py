import datetime
print("♠ 지금까지 몇 일? ♠")
day1 = datetime.date(2021,12,26)
print(day1)

today = datetime.date.today()

# 지나온 날
passedtime = today - day1
print(passedtime)
print("개강 이후 {}일이 지났습니다.".format(passedtime.days))



import calendar as cal

# 달력
cal.prcal(2021)             # 1년 달력 출력
cal.prmonth(2022,2)         # 특정 달 출력