lst = [int(i) for i in input().split( )]
x = int(input())
y = ''
c = ''
if lst.count(x) != 0:
        for i in lst:
            if i == x:
                y = lst.index(i)
                lst.insert(y,0)
                lst.remove(x)
                print(y, end = ' ')
else:
    print("Отсутствует")