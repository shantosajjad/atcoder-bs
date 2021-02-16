# AtCoder beginner's selection abc081a

num = int(input())
count_1 = 0

while num > 0:
    if num%10 == 1:
        count_1 += 1
    num //= 10
print(count_1)


