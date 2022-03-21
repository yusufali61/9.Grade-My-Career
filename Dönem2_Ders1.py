#Tuple 
iller=("Ankara","İzmir","Samsun",5,5.5,True,"Ankara")
ilceler=("Pamukova","Konak","Atakum")

print(iller[2]) #print(iller[-4]) kullanırsak yine aynısı olur
print(iller[2:4])
print(iller[1]+"-" + ilceler[1])

#Tuple'ı Listeye Çevirme
iller2=list(iller)       #eğer tuple listeye çevrilmez ise hata verir çünki tuple yazıldıktan sonra eleman eklenemez
iller2[2]="Diyarbakır"
print(iller2)

#Tuple Eleman Sorgulama
print(len(iller))

#Tuple Eleman Sayısı Bulma
print(iller2.count("Ankara"))

#Tuple Eleman İndeksi Bulma
print(ilceler.index("Atakum"))

#Tuple Birleştirme
sehirler=ilceler+iller
print(sehirler)


#Dictionary (Sözlük)
bilgi={"Ad":"Yusuf Ali","Yaş":15,"Meslek":"Öğrenci"}
sozluk={"Ant":"Yemin","Muharebe":"Savaş","Sulh":"Barış"}
sozluk1={"Ant":"Yemin","Muharebe":"Savaş","Sulh":"Barış","Anlaşma":"bir konuda uyuşma","ceza":"yapılan yanlışın karşılığı "}

print(sozluk["Ant"])  #Dictionary de index numarası alınmaz
print(bilgi["Yaş"])

print(bilgi.keys())
print(bilgi.values())

print(bilgi["Meslek"]+"-"+sozluk["Sulh"])

bilgi["Meslek"]="Polis"
print(bilgi)

print("Mesleği" in bilgi)

bilgi["Hobi"]="Kitap Okumak"
print(bilgi)

print(bilgi.pop("Hobi"))
print(bilgi)

del sozluk
#print(sozluk) del ile sözlüğü sildiğimiz için yazdıramaz

print(bilgi.clear())
print(bilgi)

yedek=sozluk1.copy()
print(yedek)

donanim = {"Türü":"RAM","Tipi":"DDR4","Kapasite":"8GB"}
donanim2 = {"Türü":"Sabit Disk","Tipi":"SSD","Kapasite":"1TB"}
donanımlarim = {"donanim1":donanim, "donanim2":donanim2}
print(donanımlarim)
print(donanim)






















