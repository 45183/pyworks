# os 모듈 - 환경 변수나 디렉터리, 파일 등의 os 자원을 제어하는 모듈

import os

os.chdir('c:/pyworks/day20')        # 경로 이동

dir = os.popen('dir')
print(dir.read())