a = int(input())
b = int(input())
d = 0
while ((a > d) or (b > d)) or ((d%a != 0) or (d%b != 0)):
    d += 1
else:
    print(d)