# 👥 User Acceptance Testing (UAT): LMS Tutoring Academy

Dokumentasi Pengujian Penerimaan Pengguna (*User Acceptance Test*) untuk menilai kesiapan sistem *standalone* LMS Tutoring Academy menggantikan proses operasional manual (sebelumnya melalui WhatsApp dan Google Drive).

---

## 1. Kriteria Penerimaan UAT (Acceptance Criteria)

| No | Kriteria Penerimaan Bisnis | Status Verifikasi | Catatan Evaluator |
|---|---|---|---|
| **1** | Pengguna dapat melakukan proses login sesuai dengan hak akses (Siswa, Tutor, Admin). | ✅ **Memenuhi Syarat** | Login multi-role bekerja sesuai pembagian kredensial. |
| **2** | Pengguna dapat menjalankan alur proses bisnis utama dari awal sampai akhir. | ⚠️ **Diterima Bersyarat** | Alur pendaftaran dan navigasi materi berjalan baik; integrasi ujian kuis dinamis perlu penuntasan backend. |
| **3** | Data yang diinputkan pengguna tersimpan secara presisi ke dalam sistem. | ✅ **Memenuhi Syarat** | Data profil dan master kelas tersimpan tanpa anomali. |
| **4** | Laporan statistik dan analitik sesuai dengan filter kebutuhan stakeholder. | ⚠️ **Dalam Penyempurnaan** | Komponen grafik UI telah sesuai; data analitik Eye Tracking membutuhkan koneksi model inference ViT. |
| **5** | Tampilan antarmuka (*UI/UX*) mudah dipahami dan intuitif bagi pengguna akhir. | ✅ **Memenuhi Syarat** | Desain responsif, clean, dan navigasi ramah pengguna (*user-friendly*). |
| **6** | Tidak ada bug berkategori *Critical* atau *High* yang menghambat aktivitas esensial pengguna. | ✅ **Memenuhi Syarat** | Tidak ada crash blocking pada fitur rilis v1.0. |

---

## 2. Formulir Pelaksanaan Skenario UAT

| No | Fitur Bisnis | Skenario UAT | Hasil yang Diharapkan (*Expected*) | Pengamatan Pengguna Akhir | Status | Catatan Pengguna |
|---|---|---|---|---|---|---|
| **1** | **Autentikasi Login** | Pengguna masuk menggunakan akun yang valid | Berhasil diarahkan ke dashboard sesuai role masing-masing | Tampilan dashboard langsung terbuka sesuai hak akses pengguna | ✅ **Pass** | Alur login cepat dan mudah dipahami |
| **2** | **Data Master Kelas** | Admin menambahkan paket kurikulum kelas baru | Data kelas baru tersimpan dan otomatis tampil di katalog siswa | Kelas baru langsung muncul di menu pilihan pembelajaran | ✅ **Pass** | Sangat membantu menggantikan pencatatan Excel |
| **3** | **Aktivitas Pembelajaran** | Siswa membuka modul materi video pembelajaran | Video materi dapat diputar lancar dan progres bertambah | Video dapat di-play tanpa buffer berlebih | ✅ **Pass** | Jauh lebih teratur dibanding link Google Drive terpisah |
| **4** | **Pencarian Materi** | Pengguna mencari modul menggunakan kata kunci | Menampilkan daftar materi spesifik yang dicari | Materi terkait keyword langsung tersaring | ⚠️ **Catatan** | Perlu perbaikan query search backend agar lebih dinamis |
| **5** | **Monitoring Dashboard** | Admin meninjau grafik aktivitas siswa di platform | Statistik keaktifan kelas tampil secara visual | Tampilan chart grafik sangat informatif dan rapi | ✅ **Pass** | Memudahkan evaluasi performa bimbingan |
| **6** | **Manajemen Sesi (Logout)** | Pengguna menekan tombol keluar dari aplikasi | Sesi otentikasi berakhir dan kembali ke halaman login | Session terhapus dan halaman langsung dialihkan ke rute login | ✅ **Pass** | Keamanan akun terjamin |

---

## 3. Rekapitulasi & Pernyataan Hasil UAT

Berdasarkan hasil pengujian penerimaan pengguna (*User Acceptance Test*) yang telah diselenggarakan bersama tim penguji dan perwakilan pengguna:

> **Pernyataan Keputusan**:  
> ☑️ **[ X ] Diterima dengan catatan minor**  
> *(Sistem dinyatakan layak digunakan untuk fase operasional bertahap, dengan catatan penyempurnaan integrasi fitur kuis real-time dan generator sertifikat otomatis pada iterasi sprint berikutnya).*

### Rekomendasi QA
1. Menyelesaikan perbaikan bug keamanan HTTP Header (CSP, CORS, X-Frame-Options) sesuai hasil audit.
2. Memfinalisasi penyambungan endpoint GraphQL Hot Chocolate pada ASP.NET Core untuk kalkulasi nilai kuis dinamis.
3. Menyiapkan modul automated testing (Selenium) untuk mempermudah regresi smoke test saat fitur baru dideploy.
