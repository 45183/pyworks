# 구구단 전체 출력
'''
for i in range(2, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i*j))
    print()
'''



# 구구단 가로 출력
'''
for i in range(1, 10):
    for j in range(2, 10):
        print("{} x  {} = {}".format(j,i,i*j), end="    ")
    print()
# 출력은 되지만 정리 x     
'''

for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %2d" % (j, i, j*i), end = "  |  ")
    print()
