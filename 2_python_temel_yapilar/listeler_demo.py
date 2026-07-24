#1
meyveler = ["Elma","Muz","Kivi","Çilek","Kiraz"]
print(meyveler[0])
print(meyveler[4])
print(meyveler[2])
print(len(meyveler))

#2
sayilar = [10,20,30,40,50,60,70,80,90]
print(sayilar[:5])
print(sayilar[6:])
print(sayilar[3:6])
print(sayilar[::-1])

#3
liste = [5,10,15]
liste.insert(1,7)
liste.append(20)
liste.remove(15)
liste.pop()
liste[0]=100
print(liste)

#4
bilgi=["Umut","Karahisar","32","İstanbul","IT"]
print(bilgi[2])
bilgi[3]="Ankara"
bilgi.append("Python")
print(bilgi)


#5
notlar = [45,80,65,90,75,100,55]
print(len(notlar))
print(notlar[0])
print(notlar[6])
print(notlar[:3])
print(notlar[4:])
notlar.append(85)
notlar[0]=50
print(notlar)

#6

sepet =[]
sepet.append("Elma")
sepet.append("Çilek")
sepet.append("Muz")
sepet.remove("Muz")
sepet.append("Karpuz")

sepet[0]="Yeşil Elma"

print(sepet)

#7

sicaklik = [28,30,31,29,27,32,33]
print(len(sicaklik))
print(sicaklik[0])
print(sicaklik[6])
print(sicaklik[:5])
print(sicaklik[5:])
print(sicaklik[::-1])
sicaklik.append(34)
sicaklik[0]=26
print(sicaklik)