def sicaklik_durumu_belirle(sicaklik: float):
    if sicaklik >= 30:
        return "Sıcak"
    elif sicaklik >= 15 and sicaklik <= 29:
        return "Ilık"
    elif sicaklik >= 0 and sicaklik <= 14:
        return "Soğuk"
    else:
        return "Dondurucu"


def giyim_onerisi_ver(sicaklik: float):
    if sicaklik >= 30:
        return "Tişört / Şort giyebilirsin"
    elif sicaklik >= 15 and sicaklik <= 29:
        return "Tişört + ince ceket iyi olur"
    elif sicaklik >= 0 and sicaklik <= 14:
        return "Mont veya kalın kazak giyebilirsin"
    else:
        return "Kalın mont, bere ve eldiven kullanmalısın"


def sonucu_yazdir(durum: str, giyim: str):

    print("----------HAVA DURUMU----------")
    print(f"Durum: {durum}")
    print(f"Giyim Önerisi: {giyim}")


# akış
sehir = input("Şehir Giriniz: ")

hava = float(input("Havanın Derecesini Giriniz: "))

durum = sicaklik_durumu_belirle(sicaklik=hava)

giyim = giyim_onerisi_ver(sicaklik=hava)

sonucu_yazdir(durum, giyim)
