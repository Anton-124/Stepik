f, z, a = int(input()), [], 0
for i in range(1,f+1):
    while a != i:
        z.append(i)
        a += 1
    a = 0
print(*z[0:f])
