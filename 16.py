a,b,c,d =map(int,input().split())
if a==b or a==c or a==d or b==c or b==d or c==d:
    print("ERROP")
elif 1900<= a*1000 + b*100 + c*10 + d <= 2050:
    print("ERROR")
else:
    print("OK")