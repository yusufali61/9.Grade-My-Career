#1-Kullanıcıdan 1 ile 5 arasında bir sayı girmesi isteyiniz. Kullanıcı 3 sayısını girdiğinde break komutu ile döngüden çıkılarak “3 sayısı girildi ve döngü sona erdi” çıktısı veren kodu yazınız.
while True:
  sayi =input("1-5 arasında bir sayı girin: ")
  if sayi == "3":
    break
 
print("3 sayısı girildi ve döngü sona erdi")

#2-Kullanıcıdan 8 karakterlik bir şifre girmesini isteyiniz. Kullanıcı 8’den az ya da daha fazla karakter içeren bir şifre girdiğinde “Şifreniz 8 karakter olmalıdır.” şeklinde uyarı verdiriniz. Kullanıcı şartlara uygun bir şifre girdiğinde de “Şifreniz kaydedildi.” uyarısı verdiriniz.
while True:
  sifre =input("8 basamaklı bir şifre girin :")
  if len(sifre) == 8:
    print("Şifreniz kaydedildi")
    break
  print("Şifreniz 8 karakter olmalıdır")

#3-Girilen metnin harflerini alt alta yazdıran Python programı
isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
else:
    print("Adının harflerini listeledim.")

#4-Python ile Sayı Tahmin Oyunu Yapımı
from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))

#5-Satır dizisini giriş olarak kabul eden ve cümledeki tüm karakterleri büyük yazdıktan sonra satırları yazdıran bir program yazın.
satirlar = []
while True:
    s = input("Giriş Yapın\n")
    if s:
        satirlar.append(s.upper())
    else:
        break;
 
for satir in satirlar:
    print (satir)

#6
i = 1
while i < 5:
  print(i)
  i += 1

#7
x = 1
while x <= 100:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1

print('bitti...')

#8
x = 0
while x < 5:    
   x+=1
   if x == 2:
       break
   print(x)

#9
x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'toplam: {result}')

#10
numbers = []
i = 0
while i<5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)