# 🔬 Detailed Equivalence Partitioning Test Cases

Dokumentasi rancangan kasus uji rinci (*Detailed Test Cases*) menggunakan teknik **Black-Box Testing — Equivalence Partitioning**, dieksekusi secara langsung oleh **Salsabil Rinaldi**.

---

## 1. Test Case: TC-001 — Registrasi Siswa

| Field Metadata | Nilai |
|---|---|
| **Identifikasi Kasus Uji** | **TC-001** |
| **Nama Kasus Uji** | Registrasi Akun Siswa Baru |
| **Metode Pengujian** | Black Box — Equivalence Partitioning |
| **Deskripsi Kasus** | Menguji proses registrasi siswa berdasarkan pembagian kelas input data valid dan invalid (partisi ekuivalen). |
| **Kondisi Awal (Pre-condition)** | Sistem berjalan normal, pengguna berada pada halaman registrasi, dan pengguna belum memiliki akun. |
| **Tanggal Pengujian** | 12 Mei 2026 |
| **Penguji (Tester)** | **Salsabil Rinaldi (J0403231073)** |

### Langkah-Langkah Prosedur Uji
1. Pengguna membuka antarmuka halaman registrasi (`/register`).
2. Pengguna memasukkan data pada field nama lengkap, email, dan kata sandi.
3. Menguji nilai input contoh: Nama `"Elysian"`, Password `"Elysian123"`.
4. Pengguna menekan tombol "Daftar".
5. Sistem memproses validasi data di sisi client dan server.

### Matriks Partisi Ekuivalen & Hasil Pengujian

| Partisi Kelas Input | Data Masukan Uji | Hasil yang Diharapkan (*Expected Result*) | Pengamatan Aktual (*Actual Result*) | Kesimpulan |
|---|---|---|---|---|
| **Valid Partition** | Nama lengkap valid, email berformat benar (`name@domain.com`), dan password memenuhi kompleksitas | Akun siswa berhasil dibuat ke database dan sistem menampilkan pesan registrasi berhasil | Akun siswa berhasil dibuat dan antarmuka memunculkan notifikasi registrasi berhasil | ✅ **Berhasil (Pass)** |
| **Invalid Partition 1** (Format Email Salah) | Email tanpa simbol `@` (contoh: `elysianemail.com`) | Sistem menolak data masukan dan menampilkan pesan peringatan format email tidak valid | Sistem memblokir proses submit dan memunculkan pesan validasi format email | ✅ **Berhasil (Pass)** |
| **Invalid Partition 2** (Field Kosong / Null) | Mengosongkan field input wajib (*mandatory fields*) | Sistem membatalkan pengiriman dan menampilkan indikator merah bahwa seluruh field wajib diisi | Sistem menampilkan pesan validasi bahwa seluruh data wajib diisi | ✅ **Berhasil (Pass)** |
| **Invalid Partition 3** (Boundary Password Pendek) | Kata sandi kurang dari batas minimum karakter (< 8 karakter) | Sistem menolak password dan menampilkan instruksi syarat minimum panjang kata sandi | Sistem menampilkan pesan bahwa password tidak memenuhi ketentuan keamanan | ✅ **Berhasil (Pass)** |

---

## 2. Test Case: TC-002 — Pengelolaan Akun & Verifikasi Email

| Field Metadata | Nilai |
|---|---|
| **Identifikasi Kasus Uji** | **TC-002** |
| **Nama Kasus Uji** | Verifikasi Email & Pengelolaan Status Akun Pengguna |
| **Metode Pengujian** | Black Box — Equivalence Partitioning |
| **Deskripsi Kasus** | Menguji kemampuan Admin dalam menonaktifkan akun pengguna atau mengubah hak akses berdasarkan data valid dan tidak valid. |
| **Kondisi Awal (Pre-condition)** | Admin telah login, data akun pengguna terdaftar tersedia, dan koneksi server normal. |
| **Tanggal Pengujian** | 12 Mei 2026 |
| **Penguji (Tester)** | **Salsabil Rinaldi (J0403231073)** |

### Langkah-Langkah Prosedur Uji
1. Admin membuka halaman Manajemen Akun (`/admin/users`).
2. Admin memilih salah satu record akun pengguna.
3. Admin memodifikasi status akun (`Active` / `Inactive`) atau mengganti peranan (*role*).
4. Admin menekan tombol "Simpan Perubahan".
5. Sistem memperbarui data pada tabel relasional user.

### Matriks Partisi Ekuivalen & Hasil Pengujian

| Skenario Uji | Kondisi Input | Hasil yang Diharapkan | Pengamatan Aktual | Kesimpulan |
|---|---|---|---|---|
| **Verifikasi Token Valid** | Membuka link verifikasi dengan token SHA valid & aktif | Status akun terverifikasi dan hak akses pengguna berhasil diaktifkan | Status akun pengguna berhasil berubah sesuai input otorisasi | ✅ **Berhasil (Pass)** |
| **Verifikasi Token Kadaluarsa** | Membuka link verifikasi dengan token sudah kedaluwarsa / acak | Sistem menolak aktivasi dan memblokir upaya login sebelum verifikasi ulang | Sistem menolak akses login pengguna yang statusnya nonaktif / token invalid | ✅ **Berhasil (Pass)** |
| **Perubahan Role Kosong** | Admin menghapus pilihan role sebelum menyimpan | Sistem menolak update dan mewajibkan pemilihan minimal satu peran pengguna | Sistem menampilkan pesan validasi bahwa hak akses wajib dipilih | ✅ **Berhasil (Pass)** |
| **Otorisasi Ilegal (Non-Admin)** | Pengguna bertipe Siswa mencoba mengirim request mutasi hak akses | Sistem memblokir request melalui middleware RBAC (*Role-Based Access Control*) | Sistem mengembalikan kode error 403 Forbidden dengan pesan akses tidak diizinkan | ✅ **Berhasil (Pass)** |

---

## 3. Test Case: TC-003 — Manajemen & Pembuatan Kelas Baru

| Field Metadata | Nilai |
|---|---|
| **Identifikasi Kasus Uji** | **TC-003** |
| **Nama Kasus Uji** | Pembuatan Kelas Pembelajaran Baru |
| **Metode Pengujian** | Black Box — Equivalence Partitioning |
| **Deskripsi Kasus** | Menguji proses pembuatan kelas baru berdasarkan kelengkapan data nama kelas, harga paket, dan penugasan tutor pengajar. |
| **Kondisi Awal (Pre-condition)** | Admin telah login dan halaman Manajemen Kelas dapat diakses. |
| **Tanggal Pengujian** | 12 Mei 2026 |
| **Penguji (Tester)** | **Salsabil Rinaldi (J0403231073)** |

### Matriks Partisi Ekuivalen & Hasil Pengujian

| Partisi Data | Kondisi Input | Hasil yang Diharapkan | Pengamatan Aktual | Kesimpulan |
|---|---|---|---|---|
| **Valid Class Record** | Nama kelas: `"Intensive UTBK 2026"`, Harga: `Rp 450.000`, Tutor: Terpilih | Data kelas tersimpan, terbit ke katalog, dan terasosiasi ke ID tutor terkait | Data kelas baru berhasil diproses dan tampil di daftar kelas | ✅ **Berhasil (Pass)** |
| **Missing Class Name** | Field nama kelas dikosongkan saat menekan tombol simpan | Sistem menolak formulir dan menampilkan penanda error pada field nama | Sistem menahan form dan memunculkan peringatan field wajib diisi | ✅ **Berhasil (Pass)** |

---

## 4. Test Case: TC-004 — Autentikasi Login Siswa Multi-Role

| Field Metadata | Nilai |
|---|---|
| **Identifikasi Kasus Uji** | **TC-004** |
| **Nama Kasus Uji** | Login Siswa Multi-Role |
| **Metode Pengujian** | Black Box — Equivalence Partitioning |
| **Deskripsi Kasus** | Menguji validasi login siswa dengan pemisahan kredensial valid dan invalid. |
| **Kondisi Awal (Pre-condition)** | Akun siswa terdaftar aktif di database. |
| **Tanggal Pengujian** | 12 Mei 2026 |
| **Penguji (Tester)** | **Salsabil Rinaldi (J0403231073)** |

### Matriks Partisi Ekuivalen & Hasil Pengujian

| Partisi Data | Data Masukan Uji | Expected Result | Actual Result | Kesimpulan |
|---|---|---|---|---|
| **Valid Credentials** | Email: `siswa@lms.com`<br>Password: `siswa123` | Login berhasil, token session tersimpan, dan diarahkan ke Dashboard Siswa | Pengguna berhasil masuk ke dashboard siswa | ✅ **Berhasil (Pass)** |
| **Wrong Password** | Email: `siswa@lms.com`<br>Password: `WrongPass!` | Sistem menolak login dan memunculkan notifikasi error kredensial | Menampilkan notifikasi "Email atau kata sandi tidak cocok" | ✅ **Berhasil (Pass)** |
