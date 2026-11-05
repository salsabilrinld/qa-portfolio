# Test Cases: Pendaftaran Santri Baru
Dokumentasi spesifikasi dan hasil pengujian fungsional formulir Pendaftaran Online Santri Baru Sistem Informasi TPQ Nurul Iman menggunakan teknik Equivalence Partitioning (EP). Formulir pendaftaran santri baru merupakan komponen proses bisnis utama untuk mendigitalkan arsip fisik calon peserta didik. Pengujian partisi ekuivalen difokuskan pada integritas format data sensitif seperti Nomor Induk Kependudukan (NIK 16 digit), validasi nomor telepon seluler orang tua, serta batas eligibilitas rentang usia santri (kelahiran tahun 2013 hingga 2020).

---

## Tabel Pelaksanaan Uji Pendaftaran Santri Baru

| Kode Skenario | Kode Hasil | Data Masukan Uji / Skenario | Hasil yang Diharapkan (*Expected Output*) | Hasil Pengujian Aktual (*Actual Output*) | Status Validasi |
|---|---|---|---|---|---|
| **A08** | **AP08** | Seluruh data form diisi lengkap dan valid:<br>- Nama: `Ardien Ferdinand`<br>- NIK: `2516021981471263` (16 digit angka)<br>- Jenis Kelamin: `Laki-laki`<br>- Tempat, Tgl Lahir: `Jakarta, 11/08/2017`<br>- Upload Berkas: `Akta.pdf` & `KK.pdf`<br>- Orang Tua: `Tegar Santoso`<br>- No HP: `085101388798`<br>- Alamat: `Jl. Bekasi, Jakarta Selatan` | Sistem menerima registrasi, menyimpan data santri ke database, dan menampilkan halaman invoice/pembayaran | Sistem menerima registrasi dan mengarahkan ke halaman pembayaran |  **Valid (Pass)** |
| **A09** | **AP09** | Form diisi dengan mengosongkan kolom wajib (NIK dikosongkan `-`) | Sistem memblokir pengiriman formulir dan menampilkan pesan: *"Please fill out this field"* | Sistem menolak submit dan memunculkan notifikasi: *"Please fill out this field"* |  **Valid (Pass)** |
| **A10** | **AP10** | Masukan NIK kurang dari 16 karakter (contoh: 15 digit `251602198147126`) | Sistem menolak data masukan dan menampilkan pesan peringatan: *"NIK harus 16 angka"* | Sistem menolak dan menampilkan pesan error: *"NIK harus 16 angka"* |  **Valid (Pass)** |
| **A11** | **AP11** | Masukan NIK mengandung karakter alfabet (contoh: `251602198147abc3`) | Sistem menolak data dan menampilkan pesan validasi: *"NIK harus 16 angka"* | Sistem menolak dan menampilkan pesan: *"NIK harus 16 angka"* |  **Valid (Pass)** |
| **A12** | **AP12** | Nomor handphone orang tua diisi karakter huruf / teks alfabet | Sistem menolak formulir dan memunculkan peringatan: *"Nomor harus berisi angka"* | Sistem meloloskan masukan dan **menerima registrasi** |  **Invalid (Fail)** |
| **A13** | **AP13** | Tanggal lahir memenuhi rentang usia santri TPQ (tahun 2013 – 2020), contoh: `11/08/2017` | Sistem memvalidasi kelayakan usia dan memproses registrasi | Sistem menerima registrasi dan melanjutkan ke tahap berikutnya |  **Valid (Pass)** |
| **A14** | **AP14** | Tanggal lahir di atas batas rentang usia (> 2020 / terlalu muda), contoh: `11/08/2021` | Sistem menolak formulir dan menampilkan pesan: *"Value must be 2020 or earlier"* | Sistem menolak dan menampilkan pesan: *"Value must be 2020 or earlier"* |  **Valid (Pass)** |
| **A15** | **AP15** | Tanggal lahir di bawah batas rentang usia (< 2013 / melampaui usia santri), contoh: `11/08/2011` | Sistem menolak formulir dan menampilkan pesan: *"Value must be 2013 or older"* | Sistem menolak dan menampilkan pesan: *"Value must be 2013 or older"* |  **Valid (Pass)** |

---

## Analisis Hasil Pengujian Modul

- Total Test Case: 8 Kasus Uji
- Status Valid (Sesuai): 7 Kasus Uji (87.5%)
- Status Invalid (Cacat / Bug): 1 Kasus Uji (12.5%) — AP12
- Temuan Kunci:
  - Validasi NIK bekerja dengan sangat ketat (panjang karakter = 16 dan wajib numerik).
  - Validasi rentang tanggal lahir (2013–2020) efektif membatasi usia pendaftar.
  - Sanitasi tipe data `tel` / regex `^[0-9]+$` pada input nomor handphone orang tua belum diterapkan di sisi controller, sehingga string huruf tetap tersimpan ke basis data.
