# 이중 for문


# 5행 5
for i in range(0, 5):
    for j in range(0, 5):
        print("$", end=" ")
    print( )


print()


# 직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, i+1):
        print("$", end=" ")
    print( )


print()

# 역직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, 5-i):
        print("$", end=" ")
    print( )
