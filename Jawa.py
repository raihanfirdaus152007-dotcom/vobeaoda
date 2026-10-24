# Daftar 10 Menu Makanan beserta Harganya
menu_makanan = {
    1: {"nama": "Bebek Ambatron", "harga": 25000},
    2: {"nama": "Soto Pak Hambali", "harga": 20000},
    3: {"nama": "Ayam Geprek khas mojokerto", "harga": 22000},
    4: {"nama": "Sate Ayam hitam Madura (10 Tusuk)", "harga": 30000},
    5: {"nama": "Bakso Urat Rusdi", "harga": 18000},
    6: {"nama": "Mie Ayam Pak Cik", "harga": 17000},
    7: {"nama": "Soto Ayam Palembang", "harga": 20000},
    8: {"nama": "Bebek Goreng Papua", "harga": 35000},
    9: {"nama": "Oggie Geprek", "harga": 28000},
    10: {"nama": "Nasi Bakar Panadol", "harga": 23000}
}

def tampilkan_menu():
    print("=" * 45)
    print("           DAFTAR MENU MAKANAN SUKI")
    print("=" * 45)
    for kode, item in menu_makanan.items():
        harga_format = f"Rp {item['harga']:,}".replace(",", ".")
        print(f"{kode:2}. {item['nama'].ljust(30)} | {harga_format}")
    print("=" * 45)

def kasir():
    pesanan = []
    
    print("\nSelamat Datang di Rumah Makan Ambatron!")
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = int(input("\nMasukkan nomor menu yang ingin dibeli (1-10): "))
            if pilihan not in menu_makanan:
                print(" Menu tidak valid! Silakan pilih nomor 1 sampai 10.")
                continue
                
            jumlah = int(input(f"Masukkan jumlah porsi untuk {menu_makanan[pilihan]['nama']}: "))
            if jumlah <= 0:
                print(" Jumlah porsi harus lebih dari 0!")
                continue
                
            nama_menu = menu_makanan[pilihan]["nama"]
            harga_satuan = menu_makanan[pilihan]["harga"]
            subtotal = harga_satuan * jumlah
            
            pesanan.append({
                "nama": nama_menu,
                "harga": harga_satuan,
                "jumlah": jumlah,
                "subtotal": subtotal
            })
            
            print(f" Berhasil menambahkan {jumlah} {nama_menu} ke keranjang.")
            
        except ValueError:
            print(" Input tidak valid! Harap masukkan angka.")
            
        tanya = input("\nIngin menambah menu lain? (y/t): ").strip().lower()
        if tanya != 'y':
            break
            
    if not pesanan:
        print("\nTerima kasih, Anda belum memesan apapun.")
        return

    total_harga = sum(item["subtotal"] for item in pesanan)
    
    # Cetak Struk Pembayaran
    print("\n" + "=" * 50)
    print("                 STRUK PEMBAYARAN")
    print("=" * 50)
    print(f"{'Menu':<22} | {'Qty':<4} | {'Subtotal':<15}")
    print("-" * 50)
    
    for item in pesanan:
        sub_str = f"Rp {item['subtotal']:,}".replace(",", ".")
        print(f"{item['nama']:<22} | {item['jumlah']:<4} | {sub_str:<15}")
        
    print("-" * 50)
    total_str = f"Rp {total_harga:,}".replace(",", ".")
    print(f"** TOTAL KESELURUHAN : {total_str} **")
    print("=" * 50)
    
    while True:
        try:
            uang_bayar = int(input("\nMasukkan jumlah uang pembeli (Rp): "))
            if uang_bayar < total_harga:
                kekurangan = total_harga - uang_bayar
                kurang_str = f"Rp {kekurangan:,}".replace(",", ".")
                print(f" Uang tidak cukup! Kurang sebesar {kurang_str}")
            else:
                kembalian = uang_bayar - total_harga
                kembali_str = f"Rp {kembalian:,}".replace(",", ".")
                bayar_str = f"Rp {uang_bayar:,}".replace(",", ".")
                
                print(f"Uang Bayar  : {bayar_str}")
                print(f"Kembalian   : {kembali_str}")
                print("\n" + "=" * 50)
                print("   TERIMA KASIH TELAH BERBELANJA DI TEMPAT KAMI!")
                print("=" * 50)
                break
        except ValueError:
            print(" Input uang tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    kasir()