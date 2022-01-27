A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0

for i in A:
    total += i
    average = total / len(A)

print(average)



customer = int(input("입장객 수 : "))

col = int(input("열의 수 : "))

if customer % col == 0:
    row = customer // col
else:
    row = customer // col +1

print("행의 수 :", row)
