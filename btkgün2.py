#LİSTS
from subprocess import list2cmdline
from tkinter import Y

liste= [1,2,3,4,5,6,7,8,9,10]
print(liste[4]) #listenin ilk elemanını gösterir. ilk elemanı 0. indis kabul edilir.
print(liste[1::2])
print(liste[::2])

print(len(liste))
print(sum(liste))
print(max(liste))
print(min(liste))

#Yukarıdaki listenin ortalamasını print ediniz.
print(sum(liste) / len(liste))

#Yukarıdaki listenin ilk yarısını toplamı ile son yarısının toplamının farkını print ediniz.
ilkyarisi= liste[:len(liste) // 2]
sonyarisi= liste[len(liste) // 2:]
print(sum(ilkyarisi) - sum(sonyarisi))

#Yukarıdaki listenin en büyük ve en küçük sayısının farkını bulunuz.
print(max(liste) - min(liste))

#listenin sonuna eleman ekler.
liste= [1,2,3,4,5,6,7,8,9,10]
liste2 =[97,98,99]
yeniliste= liste + liste2
print(yeniliste) 

print(list(range(20)))
print(list(range(10,20)))
print(list(range(10,20,30)))

#Range metodu ile 0,100 arasındaki tüm çift sayıları ekrana bastır.
print(list(range(0,100,2)))

#Range metodu ile 100,200 arasındaki tüm tek sayıları ekrana bastır.
print(list(range(101,200,2)))

#1000'den 0'a kadar 100'ün katlarını tersten ekrana basınız.
print(list(range(1000,0,-100)))


for sayi in range(100):
    print(sayi / 2)

#örnek: 0'dan 50'ye kadar tüm çift sayıların karesini ekrana basınız.
for sayi in range(0,51,2):
    print(sayi**2)
    #print(sayi * sayi)

liste=[1,2,3,4,5]
print(liste)

liste.append(10)
print(liste)

print(liste.insert(0,20))
print(liste)

liste.sort() #sort,sayıların sırasını değiştirir. küçükten büyüğe sıralar.
print(liste)

liste.sort(reverse=True) 
print(liste)

print(liste.pop())  #pop, listeden eleman silme
print(liste)

print(liste.pop(0)) #listeden 0. indisi yani ilk elemanı silme
print(liste)

liste.reverse() ##reverse, listeyi ters çevirir.
print(liste)

#örnek: insert kullanarak, append(99) yapınız.
print(liste)
liste.insert(len(liste),99)
liste.append(99) #append,listenin sonuna yeni eleman ekler.
print(liste)


liste= [1,2,3,4,5]
yeniliste =[]
for i in range(len(liste)):
    yeniliste.append(liste[i] **2)
print(yeniliste)

yeniliste= []
for i in liste:
    yeniliste.append(i**2)
print(yeniliste)

yeniliste = [i ** 2 for i in liste]
print(yeniliste)


#list comprehension ile yeniliste'nin tüm elemanlarını 1 artırın.
yeniliste2= [i + 1 for i in yeniliste]
print(yeniliste2)

yeniliste3 =[i/2 for i in yeniliste]
print(yeniliste3)

#if-else örneği
yas= int(input("yasınızı giriniz: "))
if yas <= 0 or yas > 120:
    print("yasınız geçersiz.")
elif yas >=0 and yas <= 7:
    print("okula gitmiyorsunuz")
elif yas <=8 and yas <=13:
    print("ilkokula gidiyorsun")
elif yas >=14 and yas <=18:
    print("liseye gidiyorsun")
elif yas >= 19 and yas <=25:
    print("üniversiteye gidiyorsun")
else:
    print("işe gidiyorsun")


text="hello"
for i in text:
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10):
    if i % 2 == 0:
        print(i)

#NOT:range(1, 6) 1'den 5'e kadar sayıyor,6 dahil edilmiyor.Çünkü “aralık” yarı açıktır

#WHİLE örneği
number=0
liste=[]
while number != -1:
    number = int(input("bir sayı giriniz: "))

    if number != -1:
        liste.append(number)
print(liste)
print(max(liste))
print(min(liste))
print(sum(liste) / len(liste)) 
#

x=0
while x<10:
    x += 1
    if x == 5:
        continue
    print(x)
#

import random
print(random.randrange(1,10))
print(random.randrange(1,10))

liste=[x for x in "abcdefghijklmnoprstuvwxyz"]
print(random.choice(liste))


#Kullanıcıdan input olarak bir isim alın.
#Bu ismin harfleri ve rakamları ile random bir parola oluşturun.
#Parola 10 haneli olsun. Büyük küçük harfler olabilir.(random)
isim= input("isminizi giriniz: ")
isim=isim.lower() + isim.upper() + "123645"
password =" "
for i in range(10):
    password += random.choice(isim)
print(password)

#example questions
#1- kullanıcıdan 2 adet input alın. bu iki sayıyı karşılaştırıp ekrana "küçük sayı x ve büyük sayı y" yazınız.
sayi1 =int(input("1.sayi: "))
sayi2 =int(input("2.sayi: "))

if sayi1 > sayi2:
    print("küçük sayi",sayi2, "ve büyük sayi",sayi1)
    print("küçük sayi "+ str(sayi2) + " ve büyük sayi" + str(sayi1))
    print("küçük sayi {} ve büyük sayi {}".format(sayi2,sayi1))
else:
    print("küçük sayi",sayi1, "ve büyük sayi",sayi2)
    print("küçük sayi "+ str(sayi1) + " ve büyük sayi" + str(sayi2))
    print("küçük sayi {} ve büyük sayi {}".format(sayi1,sayi2))


#2- Hileli bir zar yapınız. bu zar %50 ihtimalle 6 gelsin.
#çözüm:
import random
liste=[1,2,3,4,5,6,6,6,6,6]
deneySayisi=100
deneySonuclari =[]
for i in range(deneySayisi):
        deney=random.choice(liste)
        deneySonuclari.append(deney)
     #print(random.choice(liste))
print(deneySonuclari.count[1] / deneySayisi)
print(deneySonuclari.count[2] / deneySayisi)
print(deneySonuclari.count[3] / deneySayisi)
print(deneySonuclari.count[4] / deneySayisi)
print(deneySonuclari.count[5] / deneySayisi)
print(deneySonuclari.count[6] / deneySayisi)

#diğer çözümü:
import random
sayi= random.randint(1,2)
if sayi ==1:
    print(6)
else:
    print(random.randint(1,5))


#3- 0'dan 100'e kadar 7'nin katlarını range ile yazınız.
print(list(range(0,100,7)))


#4- 0'dan 100'e kadar 7'nin katlarını for loop ile yazınız.
for i in range(0,100,7):
    print(i)


#5- 0'dan 100'e kadar 7'nin katlarını while loop ile yazınız.
i=0
while i < 100:
    if i % 7 ==0:
        print(i)
        i += 1

#6- 0'dan 100'e kadar 7'nin katlarını bir listeye atınız. bu listedeki tüm elemanların karesini ekrana basınız.
print= list(range(0,100,7))
for i in liste:
     print( i*i)
