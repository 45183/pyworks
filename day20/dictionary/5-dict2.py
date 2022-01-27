# 딕셔너리 생성과 저장

d = {'진':30, '슈가':28}

print(d)


print()

# 요소 추가

d['지민'] = 27


# 요소 삭제 - pop()
d.pop('슈가')


# 전체 요소
for key in d:
    print(key, ':', d[key])


print()


# 모든 key 가져오기 - d.keys()
print(d.keys())
print(list(d.keys()))


print()

#모든 값 가져오기 - d.values()
print(d.values())
print(list(d.values()))


print()


# 모든 키와 값 가져오기
for key, val in d.items():
    print(key, val)
