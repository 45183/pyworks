import datetime

def get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    week_idx = datetime.date(yyyy, mm, dd).weekday()
    print(days[week_idx] + "요일")

print(get_weekday(2022, 3, 14))


now = datetime.datetime.today()             # 날짜와 시간
print(now)
print(now.year)
print(now.month)
print(now.day)

today = datetime.date.today()               # 날짜
print(today)

the_day = datetime.date(2022, 3, 13)        # 특정 날짜
print(the_day)


# 특정 날의 요일
days = ['월', '화', '수', '목', '금', '토', '일']

week_idx = datetime.date(2022, 3, 13).weekday()     # 요일
print(week_idx)                             # 0~6 : 월~일
print(days[week_idx] + "요일")
