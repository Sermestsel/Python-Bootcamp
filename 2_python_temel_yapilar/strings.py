#Strings

isim ="Umut"
sirket="Umut Yazılım"
bilgi="Python Programlama Dili" 
print(bilgi)

#String birleştirme (concatenation)

isim="Umut"
sirket="Umut Yazılım"
bilgi2=isim+" Şirketinin ismi: " + sirket
print(bilgi2)

#String ve Sayı Birleştirme

yas=32
int_to_str=str(yas) 
isim="Umut"
sonuc=isim+"'un yaşı: "+int_to_str
print(sonuc) 

#ProjeDemo: Film Bilgisi
film_adi="The Matrix"
film_yili=1999
int_to_str=str(film_yili)
imdb_puani=8.7
float_to_str=str(imdb_puani)
bilgi3=film_adi+" filmi"+" "+int_to_str+" Yılında vizyona girmiş ve izleyicilerden " +float_to_str+" puanını almıştır."
print(bilgi3)

#AynıProjenin F-string ile yazımı
film_adi="The Matrix"
film_yili=1999
imdb_puani=8.7
print(f"{film_adi} fimi {film_yili} yılında vizyona girmiş ve izleyicilerden {imdb_puani} puanını almıştır.")


accuracy= 95

print(f"Karar Ağacı accuracy: {accuracy}%")

#String İndeksleme

kelime="python"
print(kelime[0])
print(kelime[3])

#String Metotları

metin="PythoN"
metin_kucuk_harf=metin.lower()
print(metin_kucuk_harf)

#String Metot Uzunluk Bulma (ÖNEMLİ)

metin="python"
metin_uzunlugu=len(metin)
print(metin_uzunlugu)

#Yer Değiştirme/Harf Değiştirme

metin="python"
print(metin.replace("o","O"))

