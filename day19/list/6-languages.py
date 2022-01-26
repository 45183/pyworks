# for ~ in
# 컴파일러 vs 인터프리터

languages = ['Python', 'C', 'Java', 'Javascript']

for lang in languages:
    if lang in ['Python', 'Javascript']:
        print(lang + ' need interpreter')
    elif lang in ['C', 'Java']:
        print(lang + " need compiler")

# 반드시 else로 끝낼필요는 없음
# if if도 가능
