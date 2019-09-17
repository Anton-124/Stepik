a = int(input())
b = int(input())
c = int(input())
d = int(input())
for z in range(c,(d+1)):
    print('\t',z, end='')
print()
for x in range(a,(b+1)):
    print(x, end='')
    for y in range(c,(d+1)):
        print ('\t',x * y, end='')
    print()