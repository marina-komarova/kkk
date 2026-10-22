#размеры района
n,m=map(int,input().split())
#количество кварталов
k=int(input())
if k<=n*m and (k%n==0 or k%m==0):
    print("успешно")
else:
    print("неосущиствимо")