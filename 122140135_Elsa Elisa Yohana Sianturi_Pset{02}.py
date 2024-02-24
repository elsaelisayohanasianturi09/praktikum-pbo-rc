totalMahasiswa = int(input("Masukkan jumlah mahasiswa yang ingin diinputkan nilainya : "))

dataMahasiswa = {}

for i in range(totalMahasiswa):
    print(f"Data untuk mahasiswa ke-{i + 1}:")
    nama = input("Nama: ")
    nilai = float(input("Nilai: "))
    dataMahasiswa[nama] = nilai

print(f"Grade = {dataMahasiswa}")

