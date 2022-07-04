class Calisan:
    zam_orani = 1.1 
    def __init__(self,isim,soyisim,maas):

        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
        

    def bilgileri_goster(self):
        return "ad: {} Soyad: {} Maaş: {} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)
    
calisan1 = Calisan("Ali","Veli",str(5000))
calisan2 = Calisan("Yağız","Kaya",str(7400))

class Yazilimci(Calisan):

    def __init__(self, isim, soyisim, maas,bildigi_dil):
        super().__init__(isim,soyisim,maas)
        self.bildigi_dil = bildigi_dil

    zam_orani = 1.2
    def bilgileri_goster(self):
        return "ad: {} Soyad: {} Maaş: {} Email: {} Bildiği Dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)

class Yonetici(Calisan):

    def __init__(self, isim, soyisim, maas,calisanlar = None):
        super().__init__(isim, soyisim, maas)

        if calisanlar == None:
            self.calisanlar = []
        
        else:
            self.calisanlar = calisanlar

    def Calisan_Ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
            
    def Calisan_Sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def Calisanlari_Goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())

yonetici1 = Yonetici("Mehmet","Yılmaz",str(7800))


yazilimci1 = Yazilimci("Sude","Meral",str(6800),"Python")
yazilimci2 = Yazilimci("Yağız","Kaya",str(6500),"Java")


yonetici1.Calisan_Ekle(yazilimci1)
yonetici1.Calisan_Ekle(yazilimci2)

yonetici1.Calisan_Sil(calisan1)
yonetici1.Calisanlari_Goster()

yonetici2 = Yonetici("Feyyaz","Beşiktaş",1100,[yazilimci1,yazilimci2,calisan1])
yonetici2.Calisanlari_Goster()

print(isinstance(yonetici2,Yonetici))

calisan1.bilgileri_goster()
