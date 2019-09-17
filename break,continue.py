a = 0
while 1==1:
    a = int(input())
    if (a <= 100) and (a >= 10):
        print(a)
    elif a < 10:
        continue
    elif a > 100:
        break