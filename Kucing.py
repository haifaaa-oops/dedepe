from Animal import * 

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bulu, asal):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bulu = bulu 
        self.asal = asal

    def cetak_kucing(self):
        super().cetak()
        print("Bulu \t\t: ", self.bulu,
              "\nAsal \t\t: ", self.asal)

print("\n--- Kucing Siam ---")      
siam = Kucing("Siam", "Salmon", "Darat", "Melahirkan", "Tidak lebat", "Thailand")
siam.cetak_kucing()

print("\n--- Kucing Persia ---")
persia = Kucing("Persia", "Kalkun", "Darat", "Melahirkan", "Lebat", "Iran")
persia.cetak_kucing()

print("\n--- Kucing Chartreux ---")
chartreux = Kucing("Chartreux", "Royal canin", "Darat", "Melahirkan", "Agak lebat", "Prancis")
chartreux.cetak_kucing()