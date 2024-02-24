tinggiSegitiga = int(input("Masukkan tinggi segitiga : "))
for i in range(1, tinggiSegitiga):
    print((tinggiSegitiga - i) * " " + (2*i-1) * "*")