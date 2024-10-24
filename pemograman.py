# VARIABEL
harga = 0
qty = 0
total_harga = 0
diskon_persen = 0
harga_setelah_diskon = 0
pembayaran = 0
kembalian = 0

# ALGORITMA
print("JUAL BELI\n")
print("---------------------------------\n")
harga = int(input("harga barang : "))
qty = int(input("jumlah barang : "))
total_harga = harga * qty
print("total harga = ", total_harga)
diskon_persen = float(input("diskon (dalam persen) : "))
diskon = total_harga * (diskon_persen / 100)
harga_setelah_diskon = total_harga - diskon
print("harga setelah diskon = ", harga_setelah_diskon)
pembayaran = float(input("jumlah pembayaran : "))
kembalian = pembayaran - harga_setelah_diskon
print("kembalian = ", kembalian)
print("\nTerima kasih sudah berbelanja ditoko viashop!\n")