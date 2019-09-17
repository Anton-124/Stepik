x = [int(i) for i in input().split( )]
x.sort()
if len(x) == 1:
    print()
else:
    c = x
    for i in x:
        y = x.count(i)
        if (y > 1) and (c!=i):
            print(i, end=' ')
            c = i
        else:
            continue