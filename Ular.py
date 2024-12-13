from Animal import * 

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t: ", self.design,
              "\nRacun \t\t: ", self.racun)

print("\n--- Ular Anaconda ---")
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak berbisa")
anaconda.cetak_ular()

print("\n--- Ular Kobra Kuning ---")
Kobra_kuning= Ular("Kobra kuning", "Tikus", "Afrika Selatan", "Bertelur", "Corak kuning hitam", "Berbisa")
Kobra_kuning.cetak_ular()

print("\n--- Ular Lanang Sapi ---")
lanang_sapi = Ular("Lanang sapi", "Kelelawar", "Amazon", "Bertelur", "Corak garis hitam coklat", "Tidak berbisa")
lanang_sapi.cetak_ular()