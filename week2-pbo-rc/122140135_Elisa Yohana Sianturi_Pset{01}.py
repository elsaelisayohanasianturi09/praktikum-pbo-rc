import random
class Orang:
    def __init__(self, golonganDarah):
        self.golonganDarah = golonganDarah

    def alel(self):
        return self.golonganDarah[random.choice([0, 1])]

class Ayah(Orang):
    pass

class Ibu(Orang):
    pass

class Anak:
    def __init__(self, ayah, ibu):
        self.ayah = ayah
        self.ibu = ibu
        self.alelAnak = self.generate_alelAnak()

    def generate_alelAnak(self):
        alelAyah = self.ayah.alel()
        alelIbu = self.ibu.alel()

        return alelAyah + alelIbu

    def tentukan_golongan_darah(self):
        golonganDarah = "".join(sorted(self.alelAnak))
        return f"Golongan darah anak: {golonganDarah}"

inputAlelAyah = input("Masukkan alel ayah: ").upper()
inputAlelIbu = input("Masukkan alel ibu: ").upper()

ayah = Ayah(inputAlelAyah)
ibu = Ibu(inputAlelIbu)
anak = Anak(ayah, ibu)

print(f"Alel anak: {anak.alelAnak}")
print(anak.tentukan_golongan_darah())
