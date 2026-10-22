a=int(input()) #количество кнатов

b=29 #стоимость в канатах для 1 сикля
c=17*b #стоимость в канатах для 1 галлеона

galleons= a//c #количество галлеонов
ost= a%c #остаток кнатов

sickles=ost//b #количество сиклей
knats=ost%b #остаток кнатов из остатка

if galleons > 0:
    print("{galleons} галлеонов")
elif sickles > 0:
    print("{sickles} сиклей")
elif knats > 0:
    print("{knats} кнатов")

