num = int(input("Input : "))

count = 0
if num != 0:
    while num != 0:
        count = count + num*num
        num = num-1
    print(count)
else:
    print(0)
