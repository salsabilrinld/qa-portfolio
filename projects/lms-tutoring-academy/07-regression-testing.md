# 🔁 Regression Testing: LMS Tutoring Academy

Dokumentasi Pengujian Regresi (*Regression Testing*) untuk memvalidasi bahwa perbaikan bug pada sprint berjalan tidak menimbulkan efek samping (*side effects*) atau regresi pada fungsi yang telah stabil sebelumnya.

---

## Matriks Pelaksanaan Regression Test

| Regression ID | Bug / Perubahan Terkait | Area yang Diuji Ulang | Prosedur Uji Regresi | Expected Result | Actual Result | Status | Catatan QA |
|---|---|---|---|---|---|---|---|
| **REG-001** | BUG-001 & Pembaruan Skema Database | Form Tambah Data, Katalog Daftar Data, dan Modifikasi Data Kelas | 1. Input data kelas baru.<br>2. Buka daftar kelas.<br>3. Edit informasi harga kelas.<br>4. Verifikasi konsistensi record. | Data baru tersimpan dengan benar dan aksi update tidak merusak data lama | Data tersimpan dengan baik dan modifikasi record berhasil | ✅ **Pass** | Dipastikan migrasi database aman |
| **REG-002** | BUG-002 & Perbaikan Middleware Autentikasi | Alur Login Valid, Login Invalid, dan Validasi Field Kosong | 1. Coba login kredensial valid.<br>2. Coba login password salah.<br>3. Submit form login kosong. | Pesan kesalahan tampil presisi dan login kredensial valid tetap berhasil masuk | Respon validasi input sesuai harapan dan sesi login berhasil | ✅ **Pass** | Pengetatan CORS tidak memblokir akses legitimate |
| **REG-003** | Penyesuaian Routing Role Dashboard | Navigasi Halaman Siswa vs Admin | 1. Login sebagai Siswa.<br>2. Akses rute `/admin`.<br>3. Logout dan login sebagai Admin. | Siswa ditolak mengakses rute admin, admin berhasil memuat widget | Routing middleware mengisolasi hak akses peran secara presisi | ✅ **Pass** | Sesi token aman di localStorage/cookie |

---

## Kesimpulan Siklus Regresi
Semua area pengujian ulang menunjukkan hasil **Pass**. Perbaikan bug keamanan dan penyesuaian dependensi tidak mengganggu alur autentikasi maupun fungsi dasar manajemen data.
