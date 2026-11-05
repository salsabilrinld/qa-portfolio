# 🧾 Test Cases: Fitur Login — Equivalence Partitioning

Dokumentasi spesifikasi dan hasil pengujian fungsional modul Login Sistem Informasi TPQ Nurul Iman menggunakan teknik **Equivalence Partitioning (EP)** (Merujuk Tabel I dan Tabel IV pada artikel publikasi JICT).

---

## 📌 Deskripsi Pengujian
Metode pengujian *Black Box Testing* dengan teknik *Equivalence Partitioning* diterapkan karena field pada form login tidak memerlukan masukan dalam rentang angka tertentu, melainkan dikelompokkan ke dalam dua partisi dasar: **partisi valid** dan **partisi invalid**.

---

## Tabel Pelaksanaan Uji Fitur Login

| Kode Skenario | Kode Hasil | Skenario Pengujian (*Test Case*) | Data Uji Input Masukan | Hasil yang Diharapkan (*Expected Result*) | Hasil Pengujian Aktual (*Actual Result*) | Status Validasi |
|---|---|---|---|---|---|---|
| **A01** | **AP01** | Login dengan email terdaftar dan password valid | Email: `ardien0318@gmail.com`<br>Password: `ardien123` | Sistem menerima login dan menampilkan halaman dashboard | Sistem menerima login dan menampilkan halaman dashboard | ✅ **Valid (Pass)** |
| **A02** | **AP02** | Login dengan email terdaftar dan password tidak valid | Email: `ardien0318@gmail.com`<br>Password: `isabel123` | Sistem menolak login dan menampilkan indikasi kesalahan | Sistem menolak login | ✅ **Valid (Pass)** |
| **A03** | **AP03** | Login dengan email yang belum terdaftar di sistem | Email: `isa123@gmail.com`<br>Password: `isabel123` | Sistem menolak login | Sistem menolak login | ✅ **Valid (Pass)** |
| **A04** | **AP04** | Login dengan format email tidak valid (tanpa simbol `@`) | Email: `ardien0318*gmail.com`<br>Password: `ardien123` | Sistem menolak login dan menampilkan pesan validasi: *"Please include an '@' in the email address"* | Sistem menolak login dan menampilkan pesan: *"Please include an '@' in the email address"* | ✅ **Valid (Pass)** |
| **A05** | **AP05** | Login dengan field email dibiarkan kosong | Email: *(kosong)*<br>Password: `ardien123` | Sistem menolak login dan menampilkan pesan validasi: *"Please fill out this field"* | Sistem menolak login dan menampilkan pesan: *"Please fill out this field"* | ✅ **Valid (Pass)** |
| **A06** | **AP06** | Login dengan field password dibiarkan kosong | Email: `ardien0318@gmail.com`<br>Password: *(kosong)* | Sistem menolak login dan menampilkan pesan validasi: *"Please fill out this field"* | Sistem menolak login dan menampilkan pesan: *"Please fill out this field"* | ✅ **Valid (Pass)** |
| **A07** | **AP07** | Login dengan field email dan password keduanya kosong | Email: *(kosong)*<br>Password: *(kosong)* | Sistem menolak login dan menampilkan pesan validasi: *"Please fill out this field"* | Sistem menolak login dan menampilkan pesan: *"Please fill out this field"* | ✅ **Valid (Pass)** |

---

## 📊 Analisis Hasil Pengujian Modul Login

- **Total Test Case**: 7 Kasus Uji
- **Tingkat Keberhasilan**: **100% (7 / 7 Valid)**
- **Kesimpulan Fungsional**: Sistem autentikasi modul login beroperasi dengan sangat baik dalam memeriksa kombinasi kredensial pengguna, menolak format yang tidak sesuai, serta memberikan pesan kesalahan yang presisi dan informatif.
