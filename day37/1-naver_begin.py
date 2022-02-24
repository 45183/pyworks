import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
resp = requests.get(url)
# print(resp.text)
html = BeautifulSoup(resp.text, "html.parser")              # (html, 파싱)
# print(html.head)                                          # <head> 영역 출력
# print(html.title)                                         # <title> 태그 출력
# print(html.title.text)                                    # <title>의 문자열 출력

# '네이버를 시작페이지로'를 추출
div = html.find('div', attrs={'class':'service_area'})      # service_area : 네이버를 시작페이지로 부분
first_a = div.find('a')
# print(first_a)
# print(first_a.text)

# '쥬니어 네이버' 추출
all_a = div.findAll('a')
# print(all_a)
print(all_a[1].text)