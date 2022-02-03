# 동명이인 찾기 - 중복 검사

def find_same_name(a):
    same_name = []
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                same_name.append(a[i])
    return same_name

'''
a = ['콩쥐', '흥부', '팥쥐', '흥부'] 인 경우
    1행 a[0] == a[1], a[0] == a[2], a[0] == a[3]         중복 없음
    2행 a[1] == a[2], a[1] == a[3]                       중복(흥부) 발생
    3행 a[2] == a[3]                                     중복 없음
'''


name = ['콩쥐', '흥부', '팥쥐', '흥부', '콩쥐']

result = find_same_name(name)
print(result)