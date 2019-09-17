s = input()
x = 0
y = 0
while 1==1:
    if x < len(s):
        if x+1 < len(s):
            if s[x] != s[x + 1]:
                print('{}{}'.format(s[x],s[y:x + 1].count(s[x])),end='')
                x += 1
                y = x
            if (s[x] != s[x + 1]) and (s[x] != s[x-1]):
                print('{}{}'.format(s[x],s[y:x + 1].count(s[x])),end='')
                x += 1
                y = x
            if x+1 != len(s):
                if s[x] == s[x + 1]:
                    x += 1
    if x+1 == len(s):
       print('{}{}'.format(s[x],s[y:].count(s[x]), end=''))
       break