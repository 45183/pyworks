# 책 148p, Q5

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0

for score in A:
    total += score
average = total / len(A)

print(average)




# 입장객 수에 따른 줄 수 계산

customer = int(input("입장객 수 : "))

col = int(input("열의 수 : "))


if customer % col == 0:
    # row = int(custom / col)
    row = customer // col
else:
    row = int(customer / col) + 1

print("줄(행)의 수:", row)
