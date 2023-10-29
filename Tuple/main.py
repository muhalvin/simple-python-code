# Soal
print("Deskripsi : Buatlah program Tuple pada python (dinamis) dengan inputan dibawah ini!")
print("-----------------------------------------------------------------------------------")
print("T1 = 5 Nama kendaraan")
print("T2 = (10, 30, 45, 21, 12, 13, 31, 90)")
print("T3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')")
print("-----------------------------------------------------------------------------------")
print("Output 1 = Gabungkan T3 dan T1 (T3[1], T3[3], T3[4] dan T1[4], T1[2])")
print("Output 2 = Tampilkan T2[3] dan T2[5]")
print("")

# Membuat tuple T1
T1 = tuple(input(f"Masukkan 5 nama kendaraan (pisahkan dengan koma): ").split(','))

# Membuat tuple T2
T2 = (10, 30, 45, 21, 12, 13, 31, 90)

# Membuat tuple T3
T3 = ("pRaktikum", "praktikum", "Praktikum", "PraKtIkuM", "PRAKTIKUM")

# Menggabungkan T3 dan T1
O1 = (T3[1], T3[3], T3[4]) + (T1[4], T1[2])

# Output
print("Output 1: ", O1)

# Mengambil elemen dengan indeks 3 dan 5
elemen_indeks_3 = T2[3]
elemen_indeks_5 = T2[5]

# Menampilkan elemen dengan indeks 3 dan 5 masing-masing 3 kali dengan perulangan
for i in range(3):
    print("Output 2: ", elemen_indeks_3, elemen_indeks_5)