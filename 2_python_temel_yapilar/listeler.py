#Liste Tanımlaması Köşeli Parantez ile Gerçekleşir.

sayilar=[1,2,3,4,5,6]
isimler=["umut","can","yazilim","karahisar"]
karisik=["umut",1,"can",2,"karahisar",45.5] #farklı veri tiplerini aynı anda tutabilir.

print(sayilar) #[1, 2, 3, 4, 5, 6]
print(isimler) #['umut', 'can', 'yazilim', 'karahisar']
print(karisik) #['umut', 1, 'can', 2, 'karahisar', 45.5]

#Liste İndexleme : Listelerde Index 0'dan başlar.

meyveler=["elma","muz","kivi"]

print(meyveler[0]) #elma
print(meyveler[2]) #kivi
print(meyveler[-1]) #kivi

#Liste Uzunluğu
print(len(meyveler))

#Liste'de Slicing

sayilar= [10,20,30,40,50]

print(sayilar[1:4])#20'den başlar, 40'e kadar gider. [1:4] 1. indeks dahil, 4. indeks dahil değil.
print(sayilar[0:3]) #ilk üç eleman = 10,20,30
#0'dan başlanacaksa :2, elemandan diğer tarafa doğru gidecekse 2: yazılabilir. Öncesini yazmaya gerek yoktur.
print(sayilar[:3]) #ilk üç eleman = 10,20,30
print(sayilar[2:]) #30'dan sonrası


#Index Ödev Uygulaması

liste=[10,20,30,40,50,60,70,80]
print(liste[3:5])
print(liste[5:2:-1])
print(liste[:6])
print(liste[3:])

#Listeye Eleman Ekleme

sayilar=[1,2,3]
sayilar.append(4) 
print(sayilar) #[1, 2, 3, 4]

sayilar.insert(1,100) #indekse sayı ekleme yapar.
print(sayilar) #[1, 100, 2, 3, 4]

sayilar.remove(100) #eleman silme
print(sayilar) #[1, 2, 3, 4]

sayilar.pop() #en son indekste bulunan değer çıkartılır.
print(sayilar) #[1, 2, 3]

sayilar.pop(0) #belirlenen indeksi siler
print(sayilar)

sayilar[0]=999 #belirli bir indeksteki değeri başka bir değer ile değiştirir.
print(sayilar)

