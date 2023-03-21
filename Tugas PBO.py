class Mobil:
  def __init__(self, warna , merk , tahun):
    self.warna = warna
    self.merk = merk
    self.tahun = tahun

  def maju (self):
    print(f" Mobil{self.merk} berwarna {self.warna} tahun {self.tahun} berjalan maju ke jalan raya")

  def mundur(self):
    print(f"Mobil {self.merk} masuk patkiran dengan jalan mundur")

mobil_aing = Mobil("Pink","Toyota Supra",1993)
mobil_aing.maju()
mobil_aing.mundur()