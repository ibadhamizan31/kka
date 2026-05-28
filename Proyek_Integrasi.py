from abc import ABC, abstractmethod

# 1. ABSTRACTION & ENCAPSULATION
# Class abstrak ini bertindak sebagai kerangka dasar dan tidak bisa diinstansiasi secara langsung.
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        # Encapsulation: menggunakan private attribute (__harga_dasar & __stok) untuk keamanan data.
        self.__harga_dasar = harga_dasar
        self.__stok = 0 

    # Getter untuk membaca stok
    def get_stok(self):
        return self.__stok
        
    # Getter untuk harga dasar agar bisa diakses secara aman oleh child class
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Setter untuk stok dengan validasi (tidak boleh negatif)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# 2. INHERITANCE & POLYMORPHISM (LAPTOP)
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        # Memanggil constructor dari Parent Class
        super().__init__(nama, harga_dasar)
        self.processor = processor

    # Polymorphism: Override method khusus untuk Laptop (Pajak 10%)
    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total

    # Polymorphism: Override method khusus untuk tampilan Laptop
    def tampilkan_detail(self):
        pajak = 0.10 * self.get_harga_dasar()
        # Format angka menjadi Rupiah yang rapi
        h_dasar = f"Rp {int(self.get_harga_dasar()):,}".replace(',', '.')
        h_pajak = f"Rp {int(pajak):,}".replace(',', '.')
        
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: {h_dasar} | Pajak (10%): {h_pajak}")


# 3. INHERITANCE & POLYMORPHISM (SMARTPHONE)
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        # Memanggil constructor dari Parent Class
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    # Polymorphism: Override method khusus untuk Smartphone (Pajak 5%)
    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total

    # Polymorphism: Override method khusus untuk tampilan Smartphone
    def tampilkan_detail(self):
        pajak = 0.05 * self.get_harga_dasar()
        # Format angka menjadi Rupiah yang rapi
        h_dasar = f"Rp {int(self.get_harga_dasar()):,}".replace(',', '.')
        h_pajak = f"Rp {int(pajak):,}".replace(',', '.')
        
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: {h_dasar} | Pajak (5%): {h_pajak}")


# 4. FITUR KERANJANG BELANJA (Fungsi di luar class)
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    
    for i, item in enumerate(daftar_barang, 1):
        barang = item['barang']
        jumlah = item['jumlah']
        
        # Cetak nomor urut lalu panggil fungsi detail barang
        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        
        # Hitung subtotal dan format ke Rupiah
        subtotal = barang.hitung_harga_total(jumlah)
        h_subtotal = f"Rp {int(subtotal):,}".replace(',', '.')
        print(f"   Beli: {jumlah} unit | Subtotal: {h_subtotal}")
        
        total_tagihan += subtotal
        
    print(f"-------------------------------------------------")
    h_total = f"Rp {int(total_tagihan):,}".replace(',', '.')
    print(f"TOTAL TAGIHAN: {h_total}")


# ==========================================
# --- ALUR PROGRAM (USER STORY) ---
# ==========================================
print("--- SETUP DATA ---")

# 1. Admin membuat data produk (1 Laptop, 1 Smartphone)
laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15000000, "12MP")

# Setup Stok melalui Setter
laptop1.tambah_stok(10)

# 2. Admin mencoba mengisi stok dengan angka negatif (Ditolak & mendapat peringatan)
hp1.tambah_stok(-5)

# Admin kemudian mengisi stok dengan benar
hp1.tambah_stok(20)

# 3. User membeli 2 Laptop dan 1 Smartphone
# Disimpan dalam bentuk List of Dictionaries agar mudah dikirim ke keranjang belanja
keranjang_belanja = [
    {'barang': laptop1, 'jumlah': 2},
    {'barang': hp1, 'jumlah': 1}
]

# 4. Program menampilkan detail barang yang dibeli dan total harga akhir
proses_transaksi(keranjang_belanja)