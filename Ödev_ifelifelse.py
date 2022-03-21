#1) Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input('isminiz: ')
yas = int(input('yaşınız: '))
egitim = input('eğitim: ')

if (yas>=18):
    if (egitim=='lise' or egitim=='üniversite'):
        print(f'{isim} ehliyet alabilirsin.')
    else:
        print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
else:
    print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')


#2) Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdıran python uygulamasını yapınız.

yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu)/3

if (ortalama>=0) and (ortalama<25):
     print(f'ortalamanız: {ortalama} notunuz: 0')
elif (ortalama >= 25 ) and (ortalama<45):
     print(f'ortalamanız: {ortalama} notunuz: 1')
elif (ortalama >= 45 ) and (ortalama<55):
    print(f'ortalamanız: {ortalama} notunuz: 2')
elif (ortalama >= 55 ) and (ortalama<70):
    print(f'ortalamanız: {ortalama} notunuz: 3')
elif (ortalama >= 70 ) and (ortalama<85):
    print(f'ortalamanız: {ortalama} notunuz: 4')
elif (ortalama >= 85 ) and (ortalama<=100):
    print(f'ortalamanız: {ortalama} notunuz: 5')
else:
    print('yanlış bilgi girdiniz.')

#3)  Girilen bir sayının pozitif çift sayı olup olmadığını kontrol eden python uygulamasını yapınız.

sayi = int(input('sayı: '))

if (sayi > 0):
    if (sayi % 2 ==0):
        print('girilen sayı pozitif çift sayıdır.')
    else:
        print('girilen sayı pozitif ancak sayı tek.')
else:
    print('girilen sayı negatif sayı.')

#4) Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@yusufali.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

if (girilenEmail == email):
    if (girilenPassword == password):
        print('uygulamaya giriş başarılı.')
    else:
        print('parolanız yanlış')
else:
    print('email bilginiz yanlış')


#5) Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
    print(f'a en büyük sayıdır.')
elif (b > a) and (b > c):
    print(f'b en büyük sayıdır.')
elif (c > a) and (c > b):
    print(f'c en büyük sayıdır.')

#6) 8- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python uygulamasını yapınız.
#0-18.4 => Zayıf
#18.5-24.9 => Normal
#25.0-29.9 => Fazla Kilolu
#30.0-34.9 => Şişman (Obez)
name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

if (index >= 0) and (index<=18.4):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index>18.4) and (index<=24.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index>24.9) and (index<=29.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index>=29.9) and (index<=45.9):
   print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
   print('bilgileriniz yanlış.')

#7):Bir otoparkın ücret tarifesi aşağıdaki gibidir:
#1 saate kadar: 5 TL
#1-5 saat arası: Saat başı 4 TL
#5 saatten fazla: Saat başı 3 TL
saat=int(input(" Kaldığınız Süreyi Girin:"))
 
ucret=0
 
if saat <=1 :
  ucret = 5
elif saat <= 5:
  ucret = 4 * saat
else:
  ucret = 3*saat
 
print("Ödemeniz Gereken Ücret :{}".format(ucret))

#8) Yaş Örneği
yaş = int(input("Yaşınız: "))

if yaş == 18:
    print("18 iyidir!")

elif yaş < 0:
    print("Yok canım, daha neler!...")

elif yaş < 18:
    print("Genç bir kardeşimizsin!")

elif yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")
