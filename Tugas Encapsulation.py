class Mobil:
  def __init__(self, warna, merk, tahun):
      self.__warna = warna
      self.__merk = merk
      self.__tahun = tahun

  def maju(self):
      print(f"Mobil {self.__merk} berwarna {self.__warna} tahun {self.__tahun} berjalan maju ke jalan raya")

  def mundur(self):
      print(f"Mobil {self.__merk} masuk parkiran dengan jalan mundur")

  def get_warna(self):
      return self.__warna

 
  def set_warna(self, warna):
      self.__warna = warna

 
  def get_merk(self):
      return self.__merk

  def set_merk(self, merk):
      self.__merk = merk


  def get_tahun(self):
      return self.__tahun


  def set_tahun(self, tahun):
      self.__tahun = tahun


mobil_aing = Mobil("Pink", "Toyota Supra", 1993)


print(mobil_aing.get_warna())
print(mobil_aing.get_merk())
print(mobil_aing.get_tahun())


mobil_aing.set_warna("Merah")
mobil_aing.set_merk("Honda Civic")
mobil_aing.set_tahun(2005)


mobil_aing.maju()
mobil_aing.mundur()
