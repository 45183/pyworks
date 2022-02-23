import requests

# requests - python 프로그래밍 언어용 http 라이브러리
# 200 - 페이지 요청 성공
# 404 - 페이지가 없음

url = "https://www.python.org/"
url2 = "https://www.python.org/3"

response = requests.get(url)
response2 = requests.get(url2)

print(response)
print(response.status_code)
print(response2)
print(response2.status_code)


html = response.text            # html 코드 저장
print(html)