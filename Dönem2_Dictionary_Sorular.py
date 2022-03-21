sozluk={"Bilim İnsanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","Astronom":"Ali Kuşçu"}
#a)
meslekler=(sozluk.copy())
print(meslekler)

#b)
print(sozluk.values())

#c)
#print(sozluk.clear())
#print(sozluk)

#ç)
sozluk["Matematikçi"]="Cahit Arf"
print(sozluk)

#d)
print("Sanatçı" in sozluk  )

#e)
sozluk["Bilim İnsanı"]="Canan Dağdeviren"
print(sozluk)

#f)
print(sozluk["Şair"])

#c)
print(sozluk.clear())
print(sozluk)

# ÖNEMLİ TELEFONLAR ÖRNEĞİ
onemli_telefonlar = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
