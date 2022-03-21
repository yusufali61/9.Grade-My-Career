#Plaka kodu bulduran program
plaka=input("plaka kodu giriniz:")
if plaka=="06":
    print("Ankara")
elif plaka=="07":
    print("Antalya")
elif plaka=="08":
    print("Artvin")
else:
    print("Türkiye")

#Operatör Sorusu 
sayi1=int(input("Herhangi bir sayı giriniz:"))
sayi2=int(input("Herhangi bir ikinci sayı giriniz:"))
isaretler=input(" * , / , - , + :")
if(isaretler)=="+":
    print(sayi1+sayi2)
elif(isaretler)=="-":
    print(sayi1-sayi2)
elif(isaretler)=="*":
    print(sayi1*sayi2)
elif(isaretler)=="/":
    print(sayi1/sayi2)
else:
    print("İşaret Bulununamadı")

#Yaşam Süresi Süresi
dogumt=int(input("Doğum Tarihinizi Giriniz: "))
yas=2022-dogumt
if(yas>=0) and (yas<=17):
    print("Çocuk")
elif(yas>=18) and (yas<=65):
    print("Genç")
elif(66>=yas<=79):
    print("Orta Yaşlı")
elif(yas>=80):
    print("Yaşlı")
else:
    print("Hatalı Yaş Giriniz")

#Kitaptaki Sorular

#)a
sicaklik=int(input("Sıcaklık Değeri Giriniz: "))
if(sicaklik<=5):
    print("Soğuk")
elif(6>=sicaklik<=14):
    print("Ilık")
elif(sicaklik>=15):
    print("Sıcak")
else:
    print("Hata")

#b)
saat=int(input("Bekleme Sürenizi Giriniz: "))
if(saat==1):
    print("Borcunuz 5TL")
elif(1>saat<5):
    print("saat*4")
elif(5<saat):
    print("Borcunuz 3TL")
else:
    print("Hata")

#c)
kenar1=int(input("Birinci Kenarı Giriniz: "))
kenar2=int(input("İkinci Kenarı Giriniz: "))
kenar3=int(input("Üçüncü Kenarı Giriniz: "))
if(kenar1==kenar2==kenar3):
    print("Üçgeniniz Eşkenar Üçgendir")
elif(kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3):
    print("Üçgeniniz İkizkenar Üçgendir")
elif(kenar1!=kenar2!=kenar3):
    print("Üçgeniniz Çeşit Kenar Üçgendir")
else:
    print("Hata")

#ç)
boy=int(input("Lütfen Boyunuz Giriniz: "))
kilo=int(input("Lütfen Kilonuzu Giriniz: "))
VKİ=(kilo/(boy*boy))
if (18>VKİ<25):
    print("Normal Kilodasınız")
elif(25>VKİ<30):
    print("Kilolusunuz")
elif(VKİ>30):
    print("Maalesef Obezsiniz")
elif(VKİ>35):
    print("Aşırı Düzeyde Obezsiniz Acilen Doktora Görünmelisiniz")
else:
    ("Hata")

#d)
maas=int(input("Lütfen Maaşınızı Giriniz: "))
yil=int(input("Çalıştığınız Yıl Sayısını Giriniz: "))
if(0<=yil<=5):
    print(+(maas/10))
elif(6<=yil<=10):
    print(maas+(maas*15))
elif(yil>=11):
    print(maas+(maas/25))
else:
    print("Hata")  

#e)
sayi1=int(input("1.Sayıyı Giriniz: "))
sayi2=int(input("2.Sayıyı Giriniz: "))
sayi3=int(input("3.Sayıyı Giriniz: "))
if(sayi1>sayi2 and sayi1>sayi3):
    print(sayi1)
elif(sayi2>sayi1 and sayi2>sayi3):
    print(sayi2)
elif(sayi3>sayi1 and sayi3>sayi2):
    print(sayi3)
else:
    print("Hata")

#Şifre Ve Kullanıcı Adı Örneği
kullanıcı_adi=int(input("Lütfen Kullanıcı Adınızı Giriniz :"))
if(kullanıcı_adi=="yusufyyla61"):
    sifre=int(input("Lütfen Şifrenizi Giriniz"))
    if(sifre==6161):
        print("Sisteme Girişiniz Başarılı")
    else:
        print("Şifre Hatalı")
else :
    print("kullanıcı_adı Hatalı")