def check(a, b):
    l = 'abcdefgh'
    if a[0] in l and b[0] in l and abs(l.index(a[0]) - l.index(b[0])) == 1:
        return 1
    else:
        return 0

s, e = map(str, input().split('-'))

x=abs(ord(s[0])-ord(e[0])) #разница между буквами стобцов
y=abs(int(s[0])-int(e[1])) #разница между номерами строк
if (x==1 and y==2) or (x==2 and y==1):
    print('верно')
else:
    print('неверно')