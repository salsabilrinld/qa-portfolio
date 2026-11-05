# 🧾 Test Case: Halaman Login — Teknik Equivalence Partitioning

| Field | Detail |
|---|---|
| **Nama Project** | ShopEasy E-Commerce Platform |
| **Modul** | Login |
| **Teknik Testing** | Black Box — Equivalence Partitioning |
| **Dibuat oleh** | [Nama Kamu] |
| **Tanggal** | 5 November 2026 |

---

## Deskripsi

Pengujian halaman login menggunakan metode **Black Box Testing** dengan teknik **Equivalence Partitioning**. Input dibagi ke dalam kelas-kelas ekuivalen (valid dan invalid) untuk memastikan setiap partisi diuji secara representatif.

---

## Kelas Equivalence Partitioning

### Field: Email

| Partisi | Kelas | Contoh Data | Keterangan |
|---|---|---|---|
| Valid | Email terdaftar, format benar | `user@shopeasy.com` | Email ada di database & format sesuai |
| Invalid 1 | Email tidak terdaftar | `tidakada@email.com` | Email valid formatnya tapi belum terdaftar |
| Invalid 2 | Format email salah | `usershopeasy.com` | Tidak ada tanda @ |
| Invalid 3 | Field kosong | *(kosong)* | Tidak diisi sama sekali |

### Field: Password

| Partisi | Kelas | Contoh Data | Keterangan |
|---|---|---|---|
| Valid | Password benar, sesuai ketentuan (8-20 karakter) | `Test@1234` | Sesuai dengan password yang terdaftar |
| Invalid 1 | Password salah | `SalahPassword` | Tidak cocok dengan yang terdaftar |
| Invalid 2 | Password terlalu pendek (< 8 karakter) | `Test1` | Di bawah minimum karakter |
| Invalid 3 | Field kosong | *(kosong)* | Tidak diisi sama sekali |

---

## Tabel Test Case

| Test ID | Skenario Pengujian | Test Data | Langkah Pengujian | Expected Result (Hasil yang Diharapkan) | Actual Result (Hasil Aktual) | Status |
|---|---|---|---|---|---|---|
| TC-LGN-001 | Login dengan email dan password yang valid dan terdaftar | Email: `user@shopeasy.com` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan email valid 3. Masukkan password valid 4. Klik tombol "Masuk" | Pengguna berhasil login dan diarahkan ke halaman Dashboard | Pengguna berhasil login dan masuk ke Dashboard | ✅ Pass |
| TC-LGN-002 | Login dengan email yang tidak terdaftar | Email: `tidakada@email.com` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan email tidak terdaftar 3. Masukkan password 4. Klik "Masuk" | Muncul pesan error: *"Email atau password salah"* | Muncul pesan error sesuai | ✅ Pass |
| TC-LGN-003 | Login dengan format email tidak valid (tanpa @) | Email: `usershopeasy.com` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan email tanpa @ 3. Masukkan password 4. Klik "Masuk" | Muncul validasi: *"Masukkan alamat email yang valid"* | Muncul validasi browser bawaan | ✅ Pass |
| TC-LGN-004 | Login dengan email kosong | Email: *(kosong)* Password: `Test@1234` | 1. Buka halaman login 2. Kosongkan field email 3. Masukkan password 4. Klik "Masuk" | Muncul validasi: *"Email wajib diisi"* | Muncul pesan "Email wajib diisi" | ✅ Pass |
| TC-LGN-005 | Login dengan password kosong | Email: `user@shopeasy.com` Password: *(kosong)* | 1. Buka halaman login 2. Masukkan email valid 3. Kosongkan field password 4. Klik "Masuk" | Muncul validasi: *"Password wajib diisi"* | Muncul pesan "Password wajib diisi" | ✅ Pass |
| TC-LGN-006 | Login dengan email dan password kosong | Email: *(kosong)* Password: *(kosong)* | 1. Buka halaman login 2. Kosongkan semua field 3. Klik "Masuk" | Muncul validasi pada kedua field: *"Email wajib diisi"* dan *"Password wajib diisi"* | Muncul validasi pada kedua field | ✅ Pass |
| TC-LGN-007 | Login dengan password salah | Email: `user@shopeasy.com` Password: `SalahPassword` | 1. Buka halaman login 2. Masukkan email valid 3. Masukkan password salah 4. Klik "Masuk" | Muncul pesan error: *"Email atau password salah"* | Muncul pesan error sesuai | ✅ Pass |
| TC-LGN-008 | Login dengan email mengandung spasi | Email: `user @shopeasy.com` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan email dengan spasi 3. Masukkan password 4. Klik "Masuk" | Muncul validasi: *"Masukkan alamat email yang valid"* | Muncul validasi format email | ✅ Pass |
| TC-LGN-009 | Login dengan email menggunakan huruf kapital | Email: `USER@SHOPEASY.COM` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan email dengan huruf kapital 3. Masukkan password 4. Klik "Masuk" | Pengguna berhasil login (email case-insensitive) | Pengguna berhasil login | ✅ Pass |
| TC-LGN-010 | Login gagal 5x berturut-turut (account lockout) | Email: `user@shopeasy.com` Password: `Salah1` s.d. `Salah5` | 1. Buka halaman login 2. Masukkan email valid 3. Masukkan password salah 4. Ulangi 5 kali | Akun terkunci, muncul pesan: *"Akun Anda terkunci. Coba lagi dalam 30 menit."* | Akun terkunci setelah percobaan ke-5 | ✅ Pass |
| TC-LGN-011 | Login dengan SQL injection pada field email | Email: `' OR '1'='1` Password: `Test@1234` | 1. Buka halaman login 2. Masukkan SQL injection di field email 3. Klik "Masuk" | Sistem menolak input, tidak terjadi SQL injection, muncul pesan error | Sistem menolak, muncul error validasi | ✅ Pass |
| TC-LGN-012 | Klik link "Lupa Password" | — | 1. Buka halaman login 2. Klik link "Lupa Password?" | Pengguna diarahkan ke halaman reset password | Halaman reset password terbuka | ✅ Pass |

---

## Ringkasan Hasil

| Total Test Case | Pass | Fail | Blocked | Not Executed |
|---|---|---|---|---|
| 12 | 12 | 0 | 0 | 0 |

**Pass Rate: 100%**
