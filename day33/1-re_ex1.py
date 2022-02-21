import re

pattern1 = re.compile("[a-z]")             # 정규 표현식
pattern2 = re.compile("[a-z]+")            # match() 함수 : 처음 문자부터 검색 (처음 불일치시 none) - find()와 유사함
result1 = pattern1.match("afternoon")      # match 사용시 compile 필요
result2 = pattern2.match("afternoon")
print(result1)
print(result2)


pattern3 = re.compile("[a-z]+")
pattern4 = re.compile("[0-9]+\s[a-z]+")
result3 = pattern3.match("2022 python")
result4 = pattern4.match("2022 python")
print(result3)
print(result4)


# [a-z] : a~z 내에서 1개
# [a-z]+ : a~z 내에서 연결되는거
# \s : 빈 공백
# \d : [0-9]
# \w : [a-zA-Z0-9]