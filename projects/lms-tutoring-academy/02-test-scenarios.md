# Test Scenarios: LMS Tutoring Academy

Daftar Skenario Pengujian tingkat tinggi (*High-Level Test Scenarios*) yang mencakup seluruh modul sistem (F-01 hingga F-13).

---

| ID Skenario | Modul Terkait | Skenario Pengujian | Tujuan Pengujian | Prioritas |
|---|---|---|---|---|
| **SC-001** | Autentikasi (F-01) | Registrasi akun Siswa & Tutor dengan verifikasi email | Memastikan akun baru terdaftar dan terverifikasi di sistem sebelum dapat melakukan login. | **Tinggi** |
| **SC-002** | Autentikasi (F-01) | Login multi-role (Admin, Tutor, Siswa) | Memastikan setiap peran pengguna diarahkan ke dashboard yang benar sesuai hak aksesnya masing-masing. | **Tinggi** |
| **SC-003** | Manajemen Akun (F-02) | Pengelolaan status akun oleh Admin | Memastikan Admin dapat mengaktifkan, menonaktifkan, atau memodifikasi hak akses akun pengguna. | **Tinggi** |
| **SC-004** | Manajemen Kelas (F-03) | Pembuatan kelas baru, penentuan harga, dan penugasan Tutor | Memastikan kurikulum pembelajaran dan tutor yang bertanggung jawab terkonfigurasi dengan benar di sistem. | **Tinggi** |
| **SC-005** | Akses & Konten (F-07) | Pengunggahan materi ajar (Video / PDF) ke Cloud Storage | Memastikan file materi tersimpan dengan aman dan tidak mengalami kerusakan (*corrupt*) saat diakses kembali oleh pengguna. | **Tinggi** |
| **SC-006** | Akses & Konten (F-05) | Alur akses materi setelah status pembayaran aktif | Memastikan konten materi berbayar hanya dapat dibuka oleh siswa yang telah memiliki status hak akses valid. | **Tinggi** |
| **SC-007** | Eye Tracking (F-09) | Izin akses webcam dan aktivasi fitur Eye Tracking | Memastikan aplikasi web dapat mengakses hardware kamera laptop dan mendeteksi wajah siswa secara real-time. | **Tinggi** |
| **SC-008** | Eye Tracking (F-09) | Trigger pop-up peringatan saat fokus siswa hilang | Memastikan model AI *Vision Transformer (ViT)* memberikan notifikasi interupsi / peringatan ketika siswa terdistraksi atau tidak menatap layar. | **Tinggi** |
| **SC-009** | Analitik (F-10) | Pembuatan rekapitulasi statistik fokus siswa secara anonim | Memastikan akumulasi data fokus siswa teragregasi dalam grafik performa yang mudah dipahami oleh Tutor dan Admin. | **Tinggi** |
| **SC-010** | Evaluasi (F-11) | Pengerjaan kuis dan kalkulasi skor otomatis | Memastikan sistem memberikan penilaian akurat secara otomatis sesuai dengan kunci jawaban kuis yang tersimpan. | **Tinggi** |
| **SC-011** | Sertifikasi (F-08) | Pelacakan progres belajar dan penerbitan sertifikat | Memastikan sertifikat digital berformat PDF otomatis terbit hanya jika progres materi dan skor kuis telah tuntas 100%. | **Tinggi** |
| **SC-012** | Support (F-12) | Fitur Reset Password oleh Admin (*Troubleshooting*) | Memastikan alur bantuan teknis dan pemulihan akun bagi pengguna yang kehilangan akses dapat dilakukan oleh Admin. | **Sedang** |
| **SC-013** | Komunikasi (F-13) | Integrasi tautan Live Session (Zoom / Google Meet) | Memastikan tautan ruang temu daring dapat diakses langsung oleh siswa melalui jadwal kelas yang tertera. | **Sedang** |
| **SC-014** | Dashboard (F-06) | Validasi akurasi data pada widget dashboard | Memastikan widget ringkasan bisnis (Admin) dan progres belajar (Siswa) merefleksikan data transaksi riil secara real-time. | **Sedang** |
