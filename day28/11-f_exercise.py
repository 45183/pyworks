# p.180

# Q5

f1 = open("./output/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("./output/test.txt", 'r')
print(f2.read())
f2.close()


# # Q6
#
# user_input = input("저장할 내용을 입력하세요 : ")
# f = open('./output/test2.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()


# Q7
with open("./output/test3.txt", 'w') as f1:
    f1.write("Life is too short\nyou need java")
    f1.close()

with open("./output/test3.txt", 'r') as f1:
    body = "Life is too short\nyou need java"
    f1.close()

body = body.replace('java', 'python')

with open("./output/test3.txt", 'w') as f2:
    f2.write(body)
    f2.close()


