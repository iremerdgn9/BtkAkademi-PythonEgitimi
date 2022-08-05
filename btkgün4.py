#iki sayının ortalamasını bulunuz. 
def ortalama(sayi1, sayi2):
    return (sayi1 + sayi2) /2
    
print(ortalama(1,2))
print (ortalama(5,10))

#
def listeOrtalama(liste):
    return sum(liste) /len(liste)
print(listeOrtalama([1,2,3,4,5]))

#kullanıcıdan input olarak liste alma, yöntem 1:
liste=[]
while True:
    sayi =input("sayı giriniz: ")
    if sayi =="":
        break
liste.append(int(sayi))
print(liste)

#kullanıcıdan input olarak liste alma, yöntem 2:
liste=[]
uzunluk= int(int("liste uzunluğu: "))
for i in range(uzunluk):
    sayi = int(input("sayi giriniz: "))
liste.append(sayi)
print(liste)
#

#kullanıcıdan input olarak liste alma, yöntem 3:
str_list=input("liste giriniz: ")
liste=str_list.split(" ")
liste=[int(i) for i in liste]
print(liste)

#soru: 1 ile 100 arasındaki tüm sayıları kullanarak bir ortalama ekrana basın
def listeOrtalama(liste):
    return sum(liste) /len(liste)

def question3():
    for i in range(2,101):
        liste= list(range(1,i+1))
        print(listeOrtalama(liste))

question3()

# Max'ı bulma algoritması
def maksimum(liste):
    enbuyuk=liste[0]
    for i in liste:
        if i >enbuyuk:
            enbuyuk=i
            return enbuyuk
print(maksimum([56,23,15,24,86,7]))

# bir listedeki Min elemanı bulunuz.
def minimum(liste):
    enkucuk=liste[0]
    for i in liste:
        if i < enkucuk:
            enkucuk = i
            return enkucuk
print(minimum([4,5,8,85,12,65]))

# input olan bir paragraf alın. kelimeleri yazdırın.
paragraf = input("metin giriniz: ")
#print(paragraf.split())
kelimeler =paragraf.split()
for kelime in kelimeler:
    yenikelime= kelime[0].upper() + kelime[1:].lower()
    print(yenikelime)
    print("-----------------------------------------")


print(ord('a'))
print(ord('b'))
print(ord('c'))
print(chr(97))  
#1 byte 8 bit


text= "hello world"
for i in text:
    print(chr(ord(i) + 1))


#parametre olarak bir text ve sayı alan, metni sayı kadar sağa kaydıran ve return eden bir sezar şifreleme fonksiyonu yazınız.

def sezarSifreleme(text, number):
    newText=" "
    for i in text:
        newText += (chr(ord(i) + number))
    return newText

print(sezarSifreleme("merhaba",3))
print(sezarSifreleme("pdkfdlmfs",-3))

#Search algoritması
liste= [4,5,6,3,8,7,4]
arananSayi =3
bulduMu = False
for i in liste:
    if i == arananSayi:
        print("sayı bulundu. ")
        bulduMu =True
        break
    if not bulduMu:
        print("sayı bulunamadıı")


#CLASS YAPISI
class Personel():
    def __init__(self,isim):
        self.isim = isim
per1 = Personel("İrem")
per2 =Personel("Hasan")

print(per1.isim)
print(per2.isim)

per1.selamla()
per2.selamla()
##########################
class Personel():
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
    def selamla(self):
        print("merhaba",self.isim, self.soyisim)

    per1= Personel("irem","hasan")
    per1.selamla()
