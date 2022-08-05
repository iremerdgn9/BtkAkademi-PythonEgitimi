#sözlük kullanımı
sozluk ={
    "beyaz": "white",
    "kırmızı": "red",
    "siyah" : "black"
    }

print(sozluk["beyaz"])
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items)

for key, value in sozluk.items():
    print(key,value)

sozluk["mavi"] = "blue" #değer ekleme
print(sozluk)  

#SET------------------
liste= [1,2,3,4,5,6,6,6,6,7,7,8,8,8,9]
print(liste)
yeniListe =set(liste)
print(yeniListe)

a =(1,1,2) #tupple
print(a)

print(len(["hello"])) #1
print(len("hello")) #5

print("hello"[0]) #h
print(["hello"][0]) #hello

#FUNCTİONS---------------------
def f(x):
    print(2*x)

def g(a):
    print(3*a)
    f(2)
    f(4)


def f(x,y):
    result= x+x*y -1
    return result
print(f(2,3))
print(f(2,10))
print(f(5,10))

#örnek: Parametre olarak 2 adet int alan ve küçük olanı return eden minimum adında fonksiyon yazınız.
def minimum(sayi1, sayi2):
    if sayi1 < sayi2:
        return sayi1
    else:
        return sayi2
print(minimum(5,10))
print(minimum(3,0))
print(minimum(7,1))

#Kullanıcıdan 2 adet int alnız. Küçük olanı minimum fonksiyonu ile ekrana basınız.
a= int(input("1. sayı: "))
b= int(input("2. sayı: "))
print("Küçük sayı: ", minimum(a,b))

def fonksiyon(b,a):
    print(b)
    print(a)
    a=5
    b=3
    fonksiyon(a,b)


#Parametre olarak bir sayı alan ve bu sayının asal olup olmadığını bulan bir fonksiyon yazın.
def isPrime(number):
    for i in range(2,number):
        if number % i ==0:
            return False
            return True

print(isPrime(15))
print(isPrime(17))

if isPrime(17):
    print("17 bir asal sayıdır.")
#parametre olarak bir sayı alan çift ise true, tek ise false döndüren fonksiyon yazınız.
def isEven(number):
    if number %2 ==0:
        return True
    else:
        return False

def isEven2(number):
    if number %2 == 0:
        return True
        return False

#isPrime methodunu kullanarak 900.000 ile 1.000.000 arasındaki tüm asal sayıları ekrana basınız.
for i in range(900000 , 100000):
    if isPrime(i):
        print(i)

'''
Soru:Parametre olarak bir sayı alın, ve bu sayı büyüklüğünde yıldız pramidi basan fonksiyon.
n=3
*
**
***  ''' 
def pramit(n):
    for i in range(n):
        print("* " *(i+1))
pramit(5)
pramit(3)

#parametre olarak bir sayı al, ve sayının faktöriyelini return eden bir fonksiyon.
#5!=5*4*3*2*1= 120
def faktoriyel(sayi):
    cevap=1
    for i in range(1, sayi):
        cevap *= (i+1)
    return cevap
print(faktoriyel(5))

#MATH kütüphanesi
import math
math.factorial



