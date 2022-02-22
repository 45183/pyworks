import re

# 이름과 전화번호 분리
# ()는 그룹으로 분리
# group(인덱스)
str01 = "jang 010-1234-5678"
# re.compile("[0-9A-Za-z]+\s+\d{3}[-]\d{4}[-]\d{4}")
pat = re.compile("(\w+)\s+(\d{3}[-]\d{4}[-]\d{4})")         # 2칸이상 띄어쓴 경우 \s+필수, 1칸 비어있으면 \s만 해도 출력
m = pat.match(str01)
print(m.group(1))               # group(인덱스번호) - n번째 그룹
print(m.group(2))

# 표현식 - ?P<그룹이름>
# 반환 문자 - group(그룹이름)
pat2 = re.compile("(?P<name>\w+)\s+(?P<phone>\d{3}[-]\d{4}[-]\d{4})")
m2 = pat2.match(str01)
print(m2.group('name'))
print(m2.group('phone'))
