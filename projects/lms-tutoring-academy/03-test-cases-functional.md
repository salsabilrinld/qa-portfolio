# 🧾 Functional Test Cases: LMS Tutoring Academy

Matriks pengujian fungsional (*Functional Requirements Testing*) modul inti aplikasi LMS Tutoring Academy (TC-001 hingga TC-016).

---

## Tabel Pelaksanaan Uji Fungsional

| Test Case ID | Modul | Skenario Pengujian | Pre-Condition | Data Uji | Langkah Uji | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|---|---|
| **TC-001** | Autentikasi (SC-001) | Registrasi Siswa Berhasil | Pengguna belum memiliki akun terdaftar | Nama: `Budi`<br>Email: `budi@email.com`<br>Pass: `Budi123!` | 1. Buka halaman registrasi<br>2. Isi seluruh field data lengkap<br>3. Klik tombol "Daftar" | Menampilkan pesan berhasil dan data tersimpan ke database | Data tersimpan dengan munculnya notifikasi pesan berhasil | ✅ **Berhasil (Pass)** |
| **TC-002** | Autentikasi (SC-001) | Verifikasi Email Registrasi | Akun baru terdaftar (status akun `pending`) | Token verifikasi valid dari email | 1. Klik tautan verifikasi di email<br>2. Sistem memvalidasi token | Akun aktif dan pengguna diarahkan ke halaman login | Email verifikasi belum dapat terkirim oleh SMTP server | ❌ **Belum berhasil (Fail)** |
| **TC-003** | Autentikasi (SC-002) | Login Admin Multi-Role | Akun Admin sudah aktif di sistem | Email: `admin@lms.com`<br>Pass: `admin123` | 1. Buka halaman login<br>2. Masukkan kredensial Admin<br>3. Klik "Login" | Masuk ke Dashboard Admin (tampilan Metrik Bisnis) | Berhasil login dan masuk ke Dashboard Admin | ✅ **Berhasil (Pass)** |
| **TC-004** | Autentikasi (SC-002) | Login Siswa Multi-Role | Akun Siswa sudah aktif di sistem | Email: `siswa@lms.com`<br>Pass: `siswa123` | 1. Buka halaman login<br>2. Masukkan kredensial Siswa<br>3. Klik "Login" | Masuk ke Dashboard Siswa (tampilan Progres Belajar) | Berhasil login dan diarahkan ke Dashboard Siswa | ✅ **Berhasil (Pass)** |
| **TC-005** | Akses & Konten (F-07) | Pengunggahan materi (Video/PDF) ke Cloud Storage | Admin sudah login ke panel | Mengisi judul, kategori, dan memilih file PDF materi | 1. Buka formulir tambah materi<br>2. Unggah file materi<br>3. Klik "Simpan" | File terunggah ke Cloud Storage dan tersimpan di database | Sistem hanya menampilkan pesan validasi form lokal | ⚠️ **Belum terintegrasi** |
| **TC-006** | Akses & Konten (F-05) | Alur pencarian & akses materi berdasarkan keyword | Data materi tersedia di database | Keyword pencarian: `Algoritma` | 1. Buka halaman katalog materi<br>2. Ketik keyword di kolom pencarian<br>3. Klik "Cari" | Data materi yang relevan dengan keyword tampil | Data dari keyword yang dicari tidak muncul di hasil pencarian | ⚠️ **Belum terintegrasi** |
| **TC-007** | Eye Tracking (F-09) | Izin akses webcam & aktivasi fitur Eye Tracking | Pengguna login dan modul materi dibuka | Data input stream kamera laptop | 1. Buka video pembelajaran<br>2. Izinkan akses webcam pada browser<br>3. Model AI ViT mendeteksi wajah | Sistem mendeteksi koordinat mata/wajah secara real-time | Komponen streaming kamera belum tersambung ke model backend | ⚠️ **Belum terintegrasi** |
| **TC-008** | Eye Tracking (F-09) | Trigger pop-up peringatan saat fokus siswa hilang | Sesi pembelajaran aktif & webcam menyala | Simulasi mata berpaling (> threshold waktu) | 1. Siswa menoleh keluar layar<br>2. Algoritma menghitung durasi distraksi | Muncul pop-up alert: *"Tetap fokus pada pembelajaran!"* | Respon peringatan otomatis belum terpicu di UI | ⚠️ **Belum terintegrasi** |
| **TC-009** | Progress Tracking & Evaluasi (F-08) | Pembaruan progres belajar siswa secara real-time | Siswa telah login & mengakses minimal 1 materi | Progres: Video tontonan 1/2, Kuis: Selesai | 1. Login sebagai Siswa<br>2. Buka modul materi<br>3. Tonton video hingga tuntas<br>4. Kembali ke dashboard | Persentase progres modul bertambah secara otomatis | Progres belum diperbarui secara dinamis ke database | ⚠️ **Belum terintegrasi** |
| **TC-010** | Evaluasi (F-11) | Pengerjaan kuis & perhitungan skor otomatis | Siswa membuka halaman evaluasi kuis | 10 butir soal pilihan ganda | 1. Kerjakan seluruh pertanyaan<br>2. Klik tombol "Submit Kuis" | Sistem menampilkan nilai skor sesuai kunci jawaban | Skor kalkulasi belum terhubung dinamis dengan API backend | ⚠️ **Belum dinamis** |
| **TC-011** | Sertifikasi (F-11) | Penerbitan sertifikat otomatis berdasarkan kuis & progres | Siswa menyelesaikan materi & kuis | Syarat: Progres 100% & Skor ≥ Passing Grade | 1. Submit kuis evaluasi akhir<br>2. Sistem evaluasi syarat kelulusan | Status berubah menjadi "Completed" & tombol unduh sertifikat aktif | Modul generator PDF sertifikat belum terintegrasi | ⚠️ **Belum terintegrasi** |
| **TC-012** | Support (F-12) | Fitur Reset Password oleh Admin (*Troubleshooting*) | Admin login & daftar akun pengguna tersedia | User: `siswa01`<br>Password baru: `siswa123` | 1. Masuk menu Manajemen Akun<br>2. Pilih target akun siswa<br>3. Klik "Reset Password"<br>4. Simpan | Password berhasil direset dan dapat digunakan untuk login | Endpoint reset password backend belum terhubung | ⚠️ **Belum terintegrasi** |
| **TC-013** | Komunikasi (F-13) | Integrasi tautan Live Session (Zoom / GMeet) | Jadwal sesi interaktif aktif terdaftar | Tautan valid ruang temu daring | 1. Buka menu jadwal kelas<br>2. Klik tombol "Join Session" | Sistem membuka tab baru mengarah ke URL Zoom / Google Meet | Handler klik tombol belum membuka tautan eksternal | ⚠️ **Belum terintegrasi** |
| **TC-014** | Dashboard (SC-014) | Akurasi Data Widget Progres Belajar Siswa | Siswa telah menyelesaikan 1 dari 2 video (50%) | Data tontonan riil: 50% | 1. Login sebagai Siswa<br>2. Periksa tampilan widget progres belajar | Widget merefleksikan nilai 50% secara presisi | Angka tampil pada halaman namun data masih bernilai statis | ⚠️ **Belum dinamis** |
| **TC-015** | Dashboard (SC-014) | Akurasi Widget Metrik Bisnis Admin | Terdapat 5 transaksi pendaftaran kelas baru | Record transaksi database | 1. Login sebagai Admin<br>2. Periksa widget ringkasan pendapatan | Total pendapatan bertambah sesuai akumulasi harga transaksi | Grafik widget tampil namun angka masih bersumber data dummy/statis | ⚠️ **Belum dinamis** |
| **TC-016** | Dashboard (SC-014) | Sinkronisasi Perubahan Status Akun secara Real-time | Admin mengubah status akun siswa menjadi *inactive* | Status: `active` → `inactive` | 1. Admin mengubah status akun<br>2. Siswa me-refresh dashboard | Hak akses kelas siswa langsung tertutup otomatis | Tampilan status di frontend berubah namun fungsionalitas belum dinamis | ⚠️ **Belum dinamis** |

---

## Analisa Hasil Pengujian Fungsional

Dari 16 skenario fungsional yang dieksekusi:
- **Pass (Berhasil)**: 3 test case (Registrasi Dasar, Login Admin, Login Siswa)
- **Fail (Gagal)**: 1 test case (Layanan pengiriman SMTP email verifikasi belum aktif)
- **Pending Integration / Static Mock**: 12 test case (Menemukan kendala sinkronisasi antara frontend Vercel dengan controller ASP.NET Core & GraphQL backend pada fase sprint ini).

> **Nilai Tambah QA**: Hasil pengujian ini memberikan visibilitas penuh kepada Product Owner dan Tech Lead mengenai kesiapan teknis rilis, mencegah penggabungan kode prematur ke tahap produksi.
