y=1
a=0
x = [int(i) for i in input().split( )]
for i in x:
    if len(x) == 1:
        print (i)
    elif 0 < a < len(x)-1:
        print(x[y-1]+x[y+1])
        y+=1
        a+=1
    elif i == x[0]:
        print(x[1]+x[-1])
        a+=1
    elif a == len(x)-1:
        print(x[0] + x[-2])