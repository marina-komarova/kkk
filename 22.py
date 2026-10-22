#n-количество детей, k-вместимость карусели, m-время 1 поездки в мин
n,k,m=map(int,input().split())
#количество поездок
sessions=(n*2+k-1)//k
time=sessions*m
print(time)
