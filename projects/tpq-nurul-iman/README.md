# 📚 Research & Publication: Black Box Testing pada Sistem Informasi TPQ Nurul Iman

Dokumentasi penelitian dan implementasi pengujian perangkat lunak berbasis artikel jurnal ilmiah nasional di mana **Salsabil Rinaldi** bertindak sebagai **Penulis Pertama (First Author)**.

---

## 📌 Identitas Artikel & Publikasi Ilmiah

| Metadata | Rincian Publikasi |
|---|---|
| **Judul Penelitian** | **Analisis Kualitas Fungsional Sistem Informasi TPQ Nurul Iman Menggunakan Pendekatan Black Box Testing** |
| **Nama Jurnal** | **Journal of Informatics and Communications Technology (JICT)** |
| **Volume & Edisi** | Vol. 7, No. 2, Hal. 083–096, Desember 2025 |
| **ISSN / DOI** | ISSN: 2686-1089 (Online) \| DOI: [10.52661](https://doi.org/10.52661) |
| **Penulis** | **Salsabil Rinaldi¹** (*First Author*), Carissa Fathinah Balti², Dian Rizky Amalia³, Rachel Aurelliya Yahya⁴, Pandaoni Cinta Cristin⁵, Sofiyanti Indriasari⁶, Muhammad Nasir⁷ |
| **Institusi** | Program Studi Teknologi Rekayasa Perangkat Lunak, Sekolah Vokasi IPB University |
| **Metodologi Pengujian** | Black Box Testing dengan kombinasi **Equivalence Partitioning (EP)** dan **Boundary Value Analysis (BVA)** |
| **Kerangka Kerja** | Software Testing Life Cycle (STLC) Modifikasi |
| **Total Test Case** | **29 Kasus Uji (Test Cases)** |

---

## 🎯 Latar Belakang Masalah & Urgensi Pengujian

Taman Pendidikan Al-Qur'an (TPQ) Nurul Iman sebelumnya mengandalkan proses administrasi konvensional berbasis buku catatan dan formulir kertas. Praktik manual ini menimbulkan risiko kehilangan arsip fisik, tingginya probabilitas salah catat, serta lambatnya proses rekapitulasi data santri.

Penerapan Sistem Informasi TPQ Nurul Iman berbasis web bertujuan mengotomatiskan pendaftaran santri baru, pencatatan kehadiran, hingga transaksi pembayaran. Namun, sebelum sistem digunakan secara operasional penuh, pengujian perangkat lunak mutlak dilakukan guna memastikan keandalan fungsional, keamanan autentikasi, serta integritas data masukan.

---

## 🔬 Metodologi Pengujian: STLC, EP, dan BVA

Penelitian ini menerapkan kerangka kerja **Software Testing Life Cycle (STLC)** yang terdiri dari 5 tahapan sistematis:
1. **Identifikasi Sistem yang Diuji**: Menganalisis kebutuhan fungsional form login, registrasi, dan formulir pendaftaran santri baru.
2. **Membuat Test Case**: Merancang pemisahan kelas partisi ekuivalen (EP) dan penentuan nilai batas ekstrem (BVA).
3. **Eksekusi Pengujian**: Memasukkan variasi nilai input data pada antarmuka web dengan perangkat uji berkinerja stabil untuk memastikan *reproducibility*.
4. **Dokumentasi Hasil Uji & Bug**: Pencatatan sistematis mencakup ID, skenario, data uji, *expected output*, *actual output*, dan status validasi.
5. **Evaluasi & Kesimpulan**: Mengukur stabilitas dan persentase kesesuaian fungsional sistem.

```
                      [ STLC Flow Diagram ]
[Start] ──> [Identifikasi Sistem] ──> [Membuat Test Case (EP & BVA)]
                                              │
[End]   <── [Evaluasi & Kesimpulan] <── [Dokumentasi Hasil & Bug] <── [Eksekusi Pengujian]
```

---

## 📊 Matriks Modul & Distribusi 29 Kasus Uji

Pengujian menargetkan 3 modul pintu gerbang sistem informasi:

| Modul Pengujian | Teknik Black Box | Jumlah Kasus Uji | Cakupan Pengujian |
|---|---|---|---|
| **1. Modul Login Pengguna** | **Equivalence Partitioning (EP)** | **7 Test Cases** (A01–A07 / AP01–AP07) | Email valid/invalid/kosong, password valid/salah/kosong, deteksi karakter `@`. |
| **2. Modul Registrasi Akun** | **Boundary Value Analysis (BVA)** | **14 Test Cases** (B01–B14 / BP01–BP14) | Batas nama (=3, <3, =50, >50), batas password (=8, <8, =16, >16), konfirmasi sandi, dan simulasi server email. |
| **3. Pendaftaran Santri Baru** | **Equivalence Partitioning (EP)** | **8 Test Cases** (A08–A15 / AP08–AP15) | Form lengkap, NIK kosong/kurang/berhuruf, nomor HP berhuruf, dan validasi rentang usia (2013–2020). |
| **Total** | **Kombinasi EP & BVA** | **29 Test Cases** | **100% Seluruh Komponen Form Kritis** |

---

## 📈 Rekapitulasi Hasil Pengujian & Temuan Cacat (Defects)

Dari total **29 test case** yang dieksekusi:
- **Tingkat Keberhasilan (Pass / Sesuai)**: **86% (25 Kasus Uji)**
- **Tingkat Ketidaksesuaian (Fail / Anomali)**: **14% (4 Kasus Uji)**

### 🐛 Ringkasan Defek yang Ditemukan:
1. **BP04 (Field Nama Lengkap > 50 Karakter)**: Sistem meloloskan masukan nama yang melebihi batas 50 karakter alih-alih menampilkan pesan error validasi.
2. **BP10 (Field Password > 16 Karakter)**: Sistem tetap menerima kata sandi melebihi batas atas 16 karakter tanpa peringatan limitasi.
3. **AP12 (Nomor Telepon Orang Tua Berisi Huruf)**: Sistem tetap meloloskan pendaftaran santri baru meskipun field nomor telepon diisi karakter alfabet (`"Nomor harus berisi angka"` tidak terpicu).
4. **Anomali Respons Umpan Balik Server**: Dibutuhkan standarisasi pesan error validasi agar pengguna mendapatkan informasi perbaikan data secara spesifik.

---

## 📁 Daftar Dokumen Kasus Uji Terinci

- 🧾 [01. Test Cases Fitur Login (Equivalence Partitioning)](./01-test-cases-login-ep.md)
- 🧾 [02. Test Cases Fitur Registrasi Akun (Boundary Value Analysis)](./02-test-cases-register-bva.md)
- 🧾 [03. Test Cases Pendaftaran Santri Baru (Equivalence Partitioning)](./03-test-cases-pendaftaran-santri-ep.md)
- 🐛 [04. Analisis Evaluasi & Temuan Bug](./04-evaluasi-temuan-bug.md)
