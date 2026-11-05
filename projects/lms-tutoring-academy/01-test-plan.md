# 📋 Test Plan: Learning Management System (LMS) untuk Tutoring Academy

Dokumen Rencana Pengujian Perangkat Lunak (DUPL) untuk sistem standalone Learning Management System (LMS) Tutoring Academy berbasis web.

---

## 1. Identitas Dokumen & Tim Proyek

| Komponen | Keterangan |
|---|---|
| **Nama Dokumen** | Dokumen Pengujian Perangkat Lunak (DUPL) dan UAT |
| **Nama Aplikasi / Sistem** | Pembuatan Learning Management System untuk Tutoring Academy |
| **Institusi / Nama Tim** | 14th Legion / Kelompok Finesawit |
| **Versi Aplikasi** | 1.0 |
| **Versi Dokumen** | 3.0 (Final) |
| **Tanggal Pengujian** | 5 Mei 2026 – 19 Mei 2026 |
| **Tim Penguji (QA)** | **Salsabil Rinaldi (J0403231073)**, Carissa Fathinah Balti (J0403231060), Keisyah Zahra Anatasya (J0403231052), Rachel Aurelliya Yahya (J0403231098) |
| **Reviewer / Dosen Pembimbing** | Dr. Sofiyanti Indriasari S.Kom., M.Kom. & Dr. Medhanita Dewi Renanti S.Kom., M.Kom. |
| **Tim Pengembang (Developers)** | Adelia Tiara Putri, Aditya Rieyza Munif, Aubrey Nedwin Mantiri, Dzacky Fahri Hadafi |
| **Stakeholder / Pengguna Akhir** | Admin, Siswa, Tutor / Pengajar |

---

## 2. Tujuan & Ruang Lingkup Pengujian

### 2.1 Tujuan Pengujian
1. Memastikan seluruh alur **User Experience** mulai dari registrasi (F-01) hingga live session (F-13) berjalan sesuai spesifikasi kebutuhan perangkat lunak.
2. Memvalidasi akurasi fitur **Eye Tracking (F-09)** berbasis kecerdasan buatan (*Vision Transformer / ViT*) dalam mendeteksi distraksi dan memberikan respons pop-up peringatan secara tepat.
3. Memastikan integritas data pada manajemen materi (F-07) dan laporan statistik fokus belajar (F-10).
4. Menilai kesiapan sistem *standalone* ini untuk menggantikan proses operasional manual (sebelumnya melalui WhatsApp dan Google Drive) melalui **User Acceptance Test (UAT)**.

---

### 2.2 Fitur yang Diuji (In Scope)

| No | Fitur / Modul | Deskripsi Pengujian | Tingkat Prioritas |
|---|---|---|---|
| **1** | **Autentikasi (F-01)** | Registrasi akun, verifikasi email, dan login multi-role (Siswa, Tutor, Admin). | **Tinggi** |
| **2** | **Manajemen Akun & Kelas (F-02, F-03)** | Pengaturan hak akses & status user oleh Admin serta pembuatan kelas, harga, dan penugasan tutor. | **Tinggi** |
| **3** | **Akses & Konten (F-05, F-07)** | Pengunggahan materi ke cloud storage, penyusunan modul, dan progres tontonan video belajar. | **Tinggi** |
| **4** | **Eye Tracking & Analitik (F-09, F-10)** | Izin akses webcam, deteksi *threshold* fokus siswa (ViT), peringatan pop-up distraksi, dan rekap statistik anonim. | **Tinggi** |
| **5** | **Evaluasi & Sertifikasi (F-08, F-11)** | Pengerjaan kuis, kalkulasi skor otomatis, pelacakan progres belajar, dan penerbitan sertifikat digital otomatis saat 100%. | **Tinggi** |
| **6** | **Komunikasi & Support (F-12, F-13)** | Troubleshooting (fitur reset password oleh Admin), audit log, dan integrasi tautan live session (Zoom / Google Meet). | **Sedang** |
| **7** | **Role-Based Dashboard (F-06)** | Tampilan widget metrik bisnis (Admin) dan progres belajar (Siswa) secara real-time. | **Sedang** |

---

### 2.3 Fitur yang Tidak Diuji (Out of Scope)

| No | Fitur | Alasan Tidak Diuji |
|---|---|---|
| 1 | **Integrasi Midtrans (Otomatis)** | Proses *payment gateway callback* belum diintegrasikan secara penuh pada fase ini; pengujian dibatasi pada aktivasi akses kelas secara manual oleh Admin. |
| 2 | **Live Streaming Internal** | Sistem dirancang menguji tautan eksternal (Zoom / GMeet), bukan membangun server webRTC video call internal di dalam aplikasi. |

---

## 3. Strategi & Jenis Pengujian

| Jenis Pengujian | Tujuan | Aktivitas Spesifik |
|---|---|---|
| **Functional Testing** | Memastikan fungsi berjalan sesuai kebutuhan fungsional sistem. | Pengujian form registrasi, login multi-role, CRUD kelas, pengerjaan kuis, upload file materi. |
| **Non-Functional Testing** | Mengukur performa, portabilitas browser, serta keamanan aplikasi. | Pengujian waktu respon dashboard (<3 detik), proteksi SQL Injection, proteksi XSS, dan kompatibilitas Chrome/Edge/Safari. |
| **Security Auditing** | Menguji konfigurasi header HTTP dan keamanan frontend/backend. | Analisa HTTP Response Header (CSP, CORS, X-Frame-Options, External Script Inclusion). |
| **Regression Testing** | Memastikan perbaikan bug tidak merusak fungsionalitas yang sebelumnya sudah stabil. | Uji ulang alur login, penambahan data, dan edit data pasca revisi developer. |
| **User Acceptance Testing (UAT)** | Memvalidasi kesiapan sistem dari kacamata pengguna akhir (Admin, Siswa, Tutor). | Pengujian 6 skenario proses bisnis utama bersama stakeholder. |

---

## 4. Lingkungan Pengujian (Test Environment)

| Komponen | Spesifikasi / Konfigurasi |
|---|---|
| **Sistem Operasi** | Windows 11 |
| **Browser Pengujian** | Google Chrome (v120+), Mozilla Firefox, Microsoft Edge, Safari |
| **Frontend Server** | Vercel Deployment (`https://tutor-academy-alpha.vercel.app/`) |
| **Backend Server** | ASP.NET Core, GraphQL API (Hot Chocolate), Localhost |
| **Database** | MySQL (Localhost) |
| **Perangkat Uji** | Laptop dengan Webcam terintegrasi (untuk pengujian Eye Tracking) |
| **Akun Uji Tersedia** | Akun Admin (`admin@lms.com`), Akun Siswa (`siswa@lms.com`), Akun Tutor |

---

## 5. Kriteria Masuk, Keluar, dan Mitigasi Risiko

### 5.1 Entry Criteria
- [x] Dokumen Software Requirements Specification (SRS) / User Story telah disetujui.
- [x] Lingkungan pengujian Vercel (Frontend) dan API backend telah aktif dan terhubung.
- [x] Data uji master (akun Admin, Siswa, Tutor, materi kuis, dan kurikulum kelas) telah disiapkan.
- [x] Test Case dan skenario pengujian telah direview dan disetujui oleh Dosen Pembimbing.

### 5.2 Exit Criteria
- [x] Seluruh skenario pengujian prioritas tinggi telah dieksekusi 100%.
- [x] Seluruh bug dengan severity Critical dan High telah ditindaklanjuti.
- [x] Regression testing telah dijalankan setelah perbaikan bug selesai.
- [x] Lembar UAT telah dinilai dan diverifikasi oleh tim penguji dan stakeholder.

### 5.3 Risiko Pengujian & Mitigasi

| Risiko | Dampak | Tindakan Mitigasi |
|---|---|---|
| **Variasi Data Uji Kurang Lengkap** | Skenario boundary & edge case terlewatkan | Menyusun data uji mencakup data normal, boundary value, dan invalid format secara spesifik. |
| **Koneksi Staging & Backend Lokal Tidak Stabil** | Hasil pengujian fluktuatif | Mengunci versi build pada Vercel dan memastikan database lokal menggunakan migrasi skema yang sinkron. |
| **Perubahan Kebutuhan di Tengah Pengerjaan** | Test case menjadi tidak relevan | Melakukan pembaruan dokumen pengujian (DUPL versi 1.0 ke 1.1 hingga 1.2) dan verifikasi berkala bersama reviewer. |
