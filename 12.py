a=int(input("введите число до 100: "))
if a <= 14 and a >= 11:
    print(a, "попугаев")
else:
    b=a%10 #последняя цифра числа

if b==1:
    print(a,"попугай")
elif b >= 2 and b <= 4:
    print(a,"попугая")
else:
    print(a,"попугаев")