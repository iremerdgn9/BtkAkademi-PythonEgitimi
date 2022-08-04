#python gösterimleri 
print(5)

number = 6 
print(number)

print(number, type(number))

ornek_bool= True
print(ornek_bool, type(ornek_bool))

metin="Merhaba Dünya" 
print(metin, type(metin))

a=3.5
print(a, type(a))

print(5 / 2)   #virgüllü bölüm
print(5 // 2)  #tam sayı bölüm
print(3 + 5)
print(2 ** 5)   #üs
print(100 ** 0.5)  #kök

print(5 + 2 / 4)
print((5+2) / 4)
print(5 == 5)
print(5 != 5)

print(5 > 4)
print(5 < 4)

sayi=5
sayi = sayi + 1
print(sayi)

sayi*= 2
print(sayi)

#mantık operatörleri
print(True and False)
print(True or False or False)
print(not True)

#örnek
gelir=input("Gelirinizi giriniz: ")
gelir=int(gelir)
vergi_yüzdesi= 0.18
vergi = gelir * vergi_yüzdesi
print("Gelir giriniz:  ",vergi)
print(vergi)

print("hello")
print("worl'd'")
print('merhaba "dünya"')

metin="merhaba dünya"
print(metin)
print(type(metin))
print(len(metin))  #metin karakterlerinin sayısını verir,len.
 
 # tek satırlık kod satırı  """ çok satırlı kod satırı 
deneme= """  
merhaba
dünya
"""
print(deneme)


deneme2= "hello\nworld"
print(deneme2)

print(metin.upper()) #tüm karakterleri büyük harf yazar,upper.

#str fonksiyonu, değişkenleri stringe çeviriyor
#int fonksiyonu değişkenleri integera çeviriyor

print(metin[0])
print(metin[1])
print(metin[12])
print(metin[-1])  #son karakteri yazar, -2 de sondan bir önceki karakteri yazar
print(metin[0:3])
print(metin[8:len(metin)])
print(metin[8:13:2])

metin=input( "bir metin giriniz: ")
print(metin[0:len(metin):2])
print(metin[::2])
print(metin[1:2])

text1="hello"
text2="world"
text3= text1 + " " + text2
print(text3)

#if- else döngüsü
a=5
if a<3:
    print("küçük ")
elif a==3:
        print("a 3 e eşit")
else:
    print(" büyük ")

for i in range(100):  #for döngüsü
    print(i)

#örnek
yaslar_toplami= 0
for i in range(3):
    dogum_tarihi =input("dogum tarihi: ")
    yaslar_toplami += 2022 - int(dogum_tarihi)
print(yaslar_toplami / 3)
    

#EXERCİSES
#1-Bir metindeki 'a' karakter sayısını for loop ile bulunuz.
#2-Kullanıcıdan 5 adet sayı alınız ve ortalamasını bulunuz.
#3-Input olarak bir metin alan ve ilk harfini büyük, kalanları küçük yazdıran bir kod yazınız.

#1
metin= "hello world"
counter=0
for i in range(len(metin)):
    if metin[i]=='a':
        counter +=1
    print(counter)

#2
sayi1= int(input("1. sayı giriniz: "))
sayi2= int(input("2. sayı giriniz: "))
sayi3= int(input("3. sayı giriniz: "))
sayi4= int(input("4. sayı giriniz: "))
sayi5= int(input("5. sayı giriniz: "))

toplam= sayi1 + sayi2 + sayi3 + sayi4 + sayi5
ortalama =toplam /5 
print(ortalama)

#3
metin=input("metin giriniz: ")
metin=metin[0].upper() + metin[1:].lower()
print(metin)


