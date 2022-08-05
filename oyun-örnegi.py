#Belirli bir aralıkta sayıyı bulana kadar devam etsin ve pc de aradığımız sayının daha büyük mü küçük mü olduğunu bulsun bize söylesin ve kaç hamlede sayıyı bulduğumuzu ekrana yazsın.

import datetime
import math
import random

sayi = random.randint(1 , 1000)
count =0
while True:
    count += 1
    tahmin =int(input("Tahmininiz: "))
    if tahmin== sayi:
        print("tebrikler kazandınız.")
        break
    elif tahmin >sayi:
        print("daha küçük")
    else:
        print("daha büyük")
print("oyunu bitirdiniz. Hamle sayısı: ", count)


