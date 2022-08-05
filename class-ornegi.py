#Personel sınıfına isim, soyisim, yaş, cinsiyet, maaş, tckimlik, çalışma günleri özelliklerini ekleyiniz. 
#Ardından 3 tane personel nesnesi tanımlayınız.

convertWeekDays={
    1:"pazartesi",
    2:"salı",
    3:"çarşamba",
    4:"perşembe",
    5:"cuma",
    6:"cumartesi",
    7:"pazar"
}

class Personel():
    def __init__(self,isim,soyisim, yas, cinsiyet, maas, tcKimlik, calisma_günleri,yeni_maas):
        self.isim=isim
        self.soyisim =soyisim
        self.yas =yas
        self.cinsiyet =cinsiyet
        self.maas =maas
        self. tcKimlik =tcKimlik
        self.calisma_günleri=calisma_günleri
        self.yeni_maas = yeni_maas

    def printInfo(self):
        print(self.isim, self.soyisim,self.yas,"yasındadır.")
        print(self.cinsiyet,"cinsiyetindedir.")
        print("maaşı", self.maas, "tldir.")
        print("kimlik numarası", self.tcKimlik)
        gunler=[convertWeekDays[i] for i in self.calisma_günleri]
        print("yeni maaşınız: ", self.yeni_maas)
        print("çalışma günleri:", '/'.join(gunler))

# çalşma günü ekleme fonkisyonu yazınız.Gün olarak sayı alsın ve listenin içine append ile eklensin.

def maas_guncelle(self, yeni_maas):
    self.maas = yeni_maas

def calisma_gunu_ekle(self,gun):
    self.calisma_gunleri.append(gun)

per1= Personel("ahmet", "yıldız", 32, "erkek", 2000, "13456741",[1,2,3,4,5], 50000)
per2= Personel("ayşe", "yılmaz", 25, "kadın", 3500, "123456789",[1,3,5], 12500)
per1.printInfo()
per2.printInfo()

