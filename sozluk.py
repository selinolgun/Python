sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))

def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))

def sil(sözcük):
    try:
        sözlük.pop(sözcük)
    except KeyError as err:
        print(err, "kelimesi bulunamadı!")
    else:
        print("{} kelimesi sözlükten silindi!".format(sözcük))