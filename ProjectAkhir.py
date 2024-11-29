# Daftar menu dengan stok
menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000, "stok": 10},
    2: {"nama": "Ayam Bakar", "harga": 20000, "stok": 5},
    3: {"nama": "Mie Goreng", "harga": 12000, "stok": 8},
    4: {"nama": "Es Teh Manis", "harga": 5000, "stok": 20},
    5: {"nama": "Es Jeruk", "harga": 6000, "stok": 15},
}

keranjang = []
data_diri = {}

# Menambahkan informasi tentang admin yang akan melayani pelanggan
admin_pelayan = {"nama": "Budi", "role": "Admin Pelayan", "status": "Siap Melayani"}

# Menambahkan informasi tentang admin yang mengatur pemesanan di dapur
admin_dapur = {"nama": "Sari", "role": "Admin Dapur", "status": "Siap Menyiapkan Pesanan"}

def tampilkan_admin_pelayan():
    print(f"Admin Pelayan yang akan melayani: {admin_pelayan['nama']} ({admin_pelayan['role']}) - Status: {admin_pelayan['status']}")

def tampilkan_admin_dapur():
    print(f"Admin Dapur yang akan mengatur pesanan: {admin_dapur['nama']} ({admin_dapur['role']}) - Status: {admin_dapur['status']}")

def input_data_diri():
    print("\nMasukkan Data Diri Anda ")
    nama = input("Nama Lengkap: ")
    alamat = input("Alamat Pengiriman: ")
    telepon = input("Nomor Telepon: ")
    data_diri["nama"] = nama
    data_diri["alamat"] = alamat
    data_diri["telepon"] = telepon
    print("Data diri telah berhasil disimpan.")

def tampilkan_menu():
    print(" \n== Daftar menu ==")
    for key, item in menu.items():
        print(f"{key}. {item['nama']} - Rp {item['harga']} - Stok: {item['stok']}")

def pilih_menu_dan_pesan():
    id_menu = int(input("\nMasukkan nomor menu yang ingin dipesan: "))
    if id_menu in menu:
        jumlah = int(input(f"Masukkan jumlah {menu[id_menu]['nama']} yang ingin dipesan: "))
        if jumlah <= menu[id_menu]['stok']:
            keranjang.append({"id": id_menu, "nama": menu[id_menu]['nama'], "harga": menu[id_menu]['harga'], "jumlah": jumlah})
            print(f"{menu[id_menu]['nama']} sebanyak {jumlah} telah ditambahkan ke keranjang.")
        else:
            print(f"Stok {menu[id_menu]['nama']} tidak mencukupi. Stok tersedia: {menu[id_menu]['stok']}")
    else:
        print("Menu tidak ditemukan. Silakan coba lagi.")

def tampilkan_keranjang():
    if len(keranjang) <= 0:
        print("Keranjang masih kosong.")
    else:
        print(" \n== Keranjang Belanja ==")
        total_harga = 0
        for item in keranjang:
            subtotal = item["harga"] * item["jumlah"]
            total_harga += subtotal
            print(f"{item['nama']} x {item['jumlah']} = Rp {subtotal}")
        print(f"Total: Rp {total_harga}")

def update_pesanan():
    if len(keranjang) <= 0:
        print("Keranjang masih kosong. Tidak ada pesanan yang bisa diubah.")
    else:
        print("\n== Pesanan yang ada di keranjang ==")
        for index, item in enumerate(keranjang):
            print(f"{index + 1}. {item['nama']} x {item['jumlah']}")
        
        index_pesanan = int(input("Masukkan nomor pesanan yang ingin diubah: ")) - 1
        if 0 <= index_pesanan < len(keranjang):
            item_pesanan = keranjang[index_pesanan]
            print(f"Pesanan yang ingin diubah: {item_pesanan['nama']} x {item_pesanan['jumlah']}")
            aksi = input("Apakah Anda ingin mengubah jumlah (ubah) atau membatalkan pesanan (batal)? ").lower()
            if aksi == "ubah":
                jumlah_baru = int(input("Masukkan jumlah baru: "))
                if jumlah_baru <= menu[item_pesanan["id"]]["stok"]:  # Cek stok yang tersedia
                    item_pesanan["jumlah"] = jumlah_baru
                    print(f"Jumlah pesanan {item_pesanan['nama']} telah diubah menjadi {jumlah_baru}.")
                else:
                    print("Stok tidak mencukupi.")
            elif aksi == "batal":
                print(f"Pesanan {item_pesanan['nama']} dibatalkan.")
                keranjang.remove(item_pesanan)  # Hapus dari keranjang
            else:
                print("Pilihan tidak valid.")
        else:
            print("Nomor pesanan tidak valid.")

def checkout():
    if len(keranjang) <= 0:
        print("Keranjang masih kosong. Tidak ada yang bisa di-checkout.")
    elif not data_diri:
        print("Anda harus memasukkan data diri sebelum checkout.")
    else:
        tampilkan_keranjang()
        konfirmasi = input("Apakah Anda ingin melanjutkan ke pembayaran? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            # Proses checkout, stok hanya akan berkurang di sini
            for item in keranjang:
                menu[item["id"]]["stok"] -= item["jumlah"]  # Mengurangi stok sesuai dengan pesanan yang diproses
            print(f"\nTerima kasih, {data_diri['nama']} ")
            print(f"Alamat Pengiriman: {data_diri['alamat']}")
            print(f"Nomor Telepon: {data_diri['telepon']}")
            print("Pesanan Anda akan segera diproses!")
            keranjang.clear()
        else:
            print("Checkout dibatalkan.")

def aplikasi_ofood():
    while True:
        print(" OFood: Aplikasi Pemesanan Makanan Online ")
        
        # Menampilkan admin yang akan melayani dan admin dapur
        print("\n=== Admin Info ===")
        tampilkan_admin_pelayan()  # Menampilkan admin pelayan
        tampilkan_admin_dapur()    # Menampilkan admin dapur
        
        if not data_diri:  # Jika data diri belum dimasukkan
            input_data_diri()
        
        print("\n=== Menu Pilihan ===")
        print("1. Tampilkan Menu dan Pesan")
        print("2. Lihat Keranjang")
        print("3. Ubah atau Batalkan Pesanan")
        print("4. Checkout")
        print("5. Keluar")

        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            tampilkan_menu()
            pilih_menu_dan_pesan()  # Pilih menu dan langsung pesan
        elif pilihan == 2:
            tampilkan_keranjang()
        elif pilihan == 3:
            update_pesanan()
        elif pilihan == 4:
            checkout()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan O-Food!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

aplikasi_ofood()