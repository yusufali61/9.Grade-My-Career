#if-elif-else

sayi=int(input("bir sayı giriniz"))
if(sayi>0):
    print("sayı pozitiftir")
elif(sayi<0):
    print("sayı negatiftir")
else:
    print("sayı sıfıra eşittir")  

#İç İçe İfadeler
#1.Yöntem
yas=int(input("Lütfen Yaşınızı Giriniz: "))
if(20<yas<=40):
    dil=input("İngilizce Biliyor Musunuz")
    if(dil=="evet"):
        print("Tebrikler İşe Alındınız")
    else:
        print("Dil Problemi !! İşe Alınmadınız")
else:
    print("Yaş Problemi !! İşe Alınmadınız")

#2.Yöntem
yas=int(input("Lütfen Yaşınızı Giriniz: "))
dil=input("İngilizce Biliyor Musunuz ?: ")
if(20>=yas<40 and dil=="evet"):
    print("Tebrikler İşe Alındınız")
else:
    print("Maalesef Sizi İşe Alamıyoruz")
