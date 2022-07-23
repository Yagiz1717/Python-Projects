import db as db

def UrunEkle(Urunismi,UrunFiyati):
    db.Urunler.append({"id":len(db.Urunler)+1,"Urunadi":db.Urunadi,"Urunfiyatı":db.UrunFiyat})

def Guncelle(id,Urunismi,fiyat):

    for urun in db.Urunler:
        if urun["id"] == id:
            urun["Urunadi"] = Urunismi
            urun["Urunfiyati"] = fiyat
            break

def UrunleriListele(): 
    for urun in db.Urunler:
        print(f"Ürün id: {urun['id']} Ürün İsmi: {urun['Urunadi']} Ürün Fiyatı: {urun['Urunfiyat']}")

