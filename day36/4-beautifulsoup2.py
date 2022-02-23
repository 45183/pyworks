from bs4 import BeautifulSoup

# findAll() 함수 사용 - 모든 태그 요소를 찾아서 리스트로 반환함

html_str = """
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>Big Data</li>
        <li>로봇</li>
    </ul>
    <ul class='lang'>
        <li>파이썬</li>
        <li>자바</li>
        <li>자바 스크립트</li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')
uls = soup.findAll('ul')
# print(uls)

# ul = soup.find('ul')
# lis = ul.findAll('li')
# print(lis)                  # [<li>인공지능</li>, <li>Big Data</li>, <li>로봇</li>]
# print(lis[0])               # <li>인공지능</li>
# print(lis[1].text)          # Big Data

ul2 = soup.find('ul', attrs={'class':'lang'})
lis2 = ul2.findAll('li')
# print(ul2)
# print(lis2)
# print(lis2[2].text)

uls = soup.findAll('ul')
print(uls)