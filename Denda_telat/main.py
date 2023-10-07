def hitung_denda(hari_terlambat):
    # Tentukan tarif denda per hari
    tarif_harian = 2000
    tarif_mingguan = 5000

    denda_harian = 0
    denda_mingguan = 0

    if hari_terlambat == 1:
        denda_harian = tarif_harian
    elif hari_terlambat > 1:
        # Hitung jumlah minggu terlambat
        minggu_terlambat = (hari_terlambat - 7) // 7
        # Hitung sisa hari
        sisa_hari = (hari_terlambat) % 7
        # Hitung total denda harian dan mingguan
        denda_harian = tarif_harian * (hari_terlambat - 7)
        denda_mingguan = tarif_mingguan * minggu_terlambat

    total_denda = denda_harian + denda_mingguan
    return total_denda

while True:
    # Masukkan jumlah hari terlambat
    try:
        hari_terlambat = int(input("Masukkan jumlah hari terlambat: "))
    except ValueError:
        print("Input harus berupa angka.")
        continue  # Restart the loop if the input is not a valid integer

    total_denda = hitung_denda(hari_terlambat)
    print(f"Denda untuk {hari_terlambat} hari terlambat adalah: {total_denda} Rupiah")

    ulangi = input("Apakah Anda ingin mengulangi perhitungan (Y/n)? ").lower()
    if ulangi != "y" and ulangi != "Y":
        break
