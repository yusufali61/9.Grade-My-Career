iller=["ankara","izmir","mardin","muş","diyarbakır","rize","antalya"]
ilceler=["gebze","darıca","kartal"]
eleman=["yusuf","ali","ali","ali","yayla","yayla"]
eleman1=["yusuf","ali","ali","ali","yayla","yayla"]

#...append
iller.append("kastamonu")
print(iller)
iller.append(5)
print(iller)

#...extend
ilceler=["gebze","darıca","kartal"]
iller.extend(ilceler)
print(iller)
print(len(iller))

#...insert
ilceler.insert(0,"Çayırova")
print(ilceler)

#...remove
ilceler.remove("Çayırova")
print(ilceler)

iller.remove(iller[0])
print(iller)
iller.remove(iller[1])
print(iller)

#...pop
ilceler.pop(2)
print(ilceler)

iller.pop(2)
print(iller)

#...clear
iller.clear()
print(iller)

#...index
print(ilceler.index("gebze"))

#...count
say=eleman.count("ali")
print(say)

#...sort
eleman.sort()
print(eleman)
eleman.sort(reverse=True)
print(eleman)

#...reverse
eleman1.reverse()
print(eleman1)

