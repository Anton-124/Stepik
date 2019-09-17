n = int(input())
if ((n == 1) or (n%10 == 1)) and n != 11 and n%100 != 11:
    print (n,"программист")
elif ((((n == 2 or n == 3 or n == 4) or (n%10 == 2 or n%10 == 3 or n%10 == 4)) and n != 12 and n != 13 and n != 14 and n%100 != 12 and n%100 != 13 and n%100 != 14)):
    print(n,"программиста")
else:
    print (n,'программистов')