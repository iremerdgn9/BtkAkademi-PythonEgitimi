#Search algoritması- listenin içindeki sayıyı bulan,sonra da buludu veya bulunamadı yazan algoritma
from itertools import count

liste= [4,5,6,3,8,7,10]
arananSayi = 4
bulduMu = False
for i in liste:
    if i == arananSayi:
        print("sayı bulundu. ")
        bulduMu =True
        break
    if not bulduMu:
        print("sayı bulunamadıı")

#Listede elemanın kaç kere geçtiğini bulun ve print ediniz.
liste =[4,5,6,3,8,7,10,4]
arananSayi =4
counter=0
for i in liste:
    if i == arananSayi:
        counter += 1
if counter == 0:
    print("sayı listede bulunamadı ")
else:
    print("sayı listede",counter,"defa bulundu")

#Parametre olarak bir liste ve bir sayı alan fonksiyon yazınız.
#Bu fonksiyon liste içerisinde sayıların kaç kere geçtiğini bulup return etsin.
def search(liste,sayi):
    counter= 0
    for i in liste:
         if i == sayi:
            counter += 1
    return counter

liste= [4,5,6,3,8,7,10,4]
print(search(liste, 15))
print(search(liste,5))

#parametre olarak bir liste alan ve bu listeyi büyükten küçüğe sıralayıp return eden bir fonksiyon yazınız.
def sort(liste):
    yeniListe =[]
    while len(liste) > 0:
        enbuyuk = max(liste)
        yeniListe.append(enbuyuk)
        liste.remove(enbuyuk)
        print(yeniListe)
    return yeniListe

liste =[5,1,7,8,9,4,56,23,15,14,74,95,85,45]
print(sort(liste))

#Try- Except metodu
try:
    print(1 + "1")
except:
    print("hata! ")
print("*****************")

#Recursive örnek- 5 ten 1 e kadar azalarak giden sayıları ekrana yazdır.
# 1den 5 e kadar artarak yazan fonksiyon.
def exampleRecursion(n):
    if n == 0:
        return
    print(n)
    exampleRecursion(n-1)
    print(n)
exampleRecursion(5)

#örnek: factoriyel hesabı - recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))


