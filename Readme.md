Markdown
# Dokumentasi Belajar Pemrograman Berorientasi Objek (OOP) Python

Repositori ini berisi kumpulan script Python yang dirancang untuk mendemonstrasikan empat pilar utama **Object-Oriented Programming (OOP)**: **Dekapsulasi (Encapsulation)**, **Pewarisan (Inheritance)**, **Polimorfisme (Polymorphism)**, dan **Abstraksi (Abstraction)**. Pendekatan pembelajaran menggunakan studi kasus dunia video game (RPG) dan sistem manajemen toko elektronik.

---

## Daftar Isi
1. [Manajemen File & Pemetaan Konsep](#manajemen-file--pemetaan-konsep)
2. [Penjelasan Rinci Per File](#penjelasan-rinci-per-file)
   * [1. game_rpg.py (Dasar Class & Inheritance)](#1-game_rpgpy-dasar-class--inheritance)
   * [2. cheat.py (Encapsulation & Validasi Data)](#2-cheatpy-encapsulation--validasi-data)
   * [3. Hero_Mole.py (Polymorphism & Method Overriding)](#3-hero_molepy-polymorphism--method-overriding)
   * [4. abc.py (Abstraction & Abstract Class)](#4-abcpy-abstraction--abstract-class)
   * [5. Proyek_Integrasi.py (Studi Kasus Gabungan)](#5-proyek_integrasipy-studi-kasus-gabungan)

---

## Manajemen File & Pemetaan Konsep

| Nama File | Pilar OOP Utama | Fokus Materi |
| :--- | :--- | :--- |
| `game_rpg.py` | Dasar OOP & *Inheritance* | Pembuatan Class, Object, Instance Method, dan Pewarisan Anak Class (`super()`). |
| `cheat.py` | *Encapsulation* | Penggunaan Private Attribute (`__`), Setter, Getter, dan Proteksi Data. |
| `Hero_Mole.py` | *Polymorphism* | *Method Overriding* dan eksekusi dinamis dalam struktur perulangan (*Loop*). |
| `abc.py` | *Abstraction* | Kontrak arsitektur kode menggunakan modul `abc` (*Abstract Base Class*). |
| `Proyek_Integrasi.py`| **Semua Pilar** | Implementasi dunia nyata menyatukan seluruh konsep ke dalam sistem transaksi toko digital. |

---

## Penjelasan Rinci Per File

### 1. game_rpg.py (Dasar Class & Inheritance)
File ini dibagi menjadi 3 bagian analisis yang mengajarkan evolusi pembuatan objek dari tingkat dasar hingga relasi orang tua-anak (*Parent-Child Class*).

* **Tugas Analisis 1 & 2 (Dasar Objek):**
    * Membuat blueprint `Hero` dengan atribut: `name`, `hp`, dan `attack_power`.
    * Metode `serang()` menerima parameter berupa objek hero lawan (`lawan`), lalu secara dinamis memicu pengurangan HP pada objek tersebut melalui metode `diserang()`.
* **Tugas Analisis 3 (Inheritance):**
    * Membuat class `Mage` yang mewarisi seluruh sifat class `Hero` menggunakan perintah `super().__init__()`.
    * `Mage` memperluas fungsionalitas dengan menambahkan atribut baru (`mana`) dan metode spesifik `skill_fireball()` yang memberikan daya rusak (damage) 2x lipat jika kapasitas mana mencukupi.

---

### 2. cheat.py (Encapsulation & Validasi Data)
File ini berfokus pada keamanan data objek. Atribut sensitif seperti HP (Health Points) diproteksi agar tidak bisa diubah secara sembarangan dari luar class.

* **Mekanisme Private Attribute:**
    * Penggunaan dua garis bawah (`self.__hp`) membuat variabel tersebut terisolasi (private). Upaya mengubah langsung seperti `hero1.__hp = 9999` akan diabaikan oleh Python atau menghasilkan error.
* **Akses Terkontrol (Getter & Setter):**
    * **Getter (`get_hp`):** Metode resmi untuk membaca nilai HP saat ini.
    * **Setter (`set_hp`):** Gerbang validasi. Jika nilai baru di bawah `0`, HP otomatis diatur ke `0`. Jika ada upaya memanipulasi HP secara tidak wajar (> 1000), sistem mendeteksi cheat dan membatasi HP maksimal di angka `1000`.

---

### 3. Hero_Mole.py (Polymorphism & Method Overriding)
File ini mendemonstrasikan bagaimana satu perintah yang sama dapat menghasilkan respons atau perilaku yang berbeda, tergantung objek mana yang mengeksekusinya.

* **Method Overriding:**
    * Class induk `Hero` memiliki metode `serang()` default (tangan kosong).
    * Class anak (`Mage`, `Archer`, `Fighter`) menulis ulang (*override*) metode `serang()` sesuai karakteristik masing-masing (menembak bola api, memanah, atau menebas dengan pedang).
* **Eksekusi Polimorfik:**
    * Seluruh objek anak dimasukkan ke dalam satu List bernama `pasukan`.
    * Menggunakan perulangan `for pahlawan in pasukan:`, program cukup memanggil `pahlawan.serang()`. Python secara cerdas mendeteksi tipe objek asli di dalam list dan mengeluarkan output serangan yang berbeda secara otomatis.

---

### 4. abc.py (Abstraction & Abstract Class)
File ini memperkenalkan konsep arsitektur perangkat lunak berupa pembuatan "kontrak wajib" menggunakan modul bawaan Python `abc` (*Abstract Base Class*).

* **Abstract Class (`GameUnit`):**
    * Class ini tidak dapat diinstansiasi menjadi objek langsung (`unit = GameUnit()` akan menghasilkan error). Fungsinya murni sebagai cetak biru abstrak.
* **Abstract Method (`@abstractmethod`):**
    * Metode `serang()` dan `info()` dideklarasikan tanpa isi (`pass`).
    * **Konsekuensi:** Setiap class konkret yang diturunkan dari `GameUnit` (seperti `Hero` dan `Monster`) **wajib** mengimplementasikan ulang metode `serang()` dan `info()`. Jika alpa, Python akan menolak menjalankan program dan melempar *TypeError*.

---

### 5. Proyek_Integrasi.py (Studi Kasus Gabungan)
File puncak yang menggabungkan seluruh konsep OOP ke dalam sebuah simulasi aplikasi kasir / manajemen inventaris toko barang elektronik.

* **Penerapan Pilar OOP di Dalam Kode:**
    1.  **Abstraction:** Class `BarangElektronik` ditandai sebagai `ABC`. Menyediakan cetak biru wajib metode `tampilkan_detail()` dan `hitung_harga_total()`.
    2.  **Encapsulation:** Atribut harga dasar (`__harga_dasar`) dan stok (`__stok`) bersifat private. Stok hanya bisa ditambah lewat metode `tambah_stok()` yang dilengkapi logika validasi anti-nilai negatif.
    3.  **Inheritance:** Class `Laptop` dan `Smartphone` mewarisi properti dasar dari `BarangElektronik`.
    4.  **Polymorphism:** Metode `hitung_harga_total()` dan `tampilkan_detail()` di-override oleh masing-masing class anak. `Laptop` menghitung komponen pajak sebesar **10%**, sedangkan `Smartphone` mengenakan pajak sebesar **5%**.
* **Alur Program (User Story):**
    * Sistem melakukan setup data produk dan melakukan validasi pengisian stok.
    * Fungsi luar `proses_transaksi()` mengumpulkan keranjang belanja (kumpulan objek barang dan jumlah beli), menghitung subtotal masing-masing produk secara polimorfik, mengubah format angka ke format Rupiah (`Rp 20.000.000`), dan mencetak struk belanja akhir.

---

## Cara Menjalankan Script
Pastikan Anda sudah menginstal Python di komputer Anda. Buka terminal atau command prompt, lalu jalankan salah satu file menggunakan perintah berikut:

```bash
# Menjalankan simulasi dasar RPG
python game_rpg.py

# Menjalankan demonstrasi enkapsulasi data
python cheat.py

# Menjalankan demonstrasi polimorfisme perang hero
python Hero_Mole.py

# Menjalankan demonstrasi abstract class
python abc.py

# Menjalankan proyek integrasi toko elektronik
python Proyek_Integrasi.py