# Evaluasi Hasil Pengujian & Temuan Cacat (Defect Analysis)
Laporan analisis evaluasi kualitas fungsional dan dokumentasi cacat sistem (*Defects*) pada Sistem Informasi TPQ Nurul Iman berdasarkan hasil pengujian 29 kasus uji kombinasi Equivalence Partitioning dan Boundary Value Analysis.

---

## Statistik Keseluruhan Pengujian

| Komponen Modul | Teknik Testing | Jumlah Test Case | Pass (Sesuai) | Fail (Invalid / Bug) | Persentase Lolos |
|---|---|---|---|---|---|
| Modul Login Pengguna | Equivalence Partitioning | 7 | 7 | 0 | 100% |
| Modul Registrasi Akun | Boundary Value Analysis | 14 | 12 | 2 | 85.7% |
| Pendaftaran Santri Baru | Equivalence Partitioning | 8 | 7 | 1 | 87.5% |
| **Total Akumulasi** | **Kombinasi EP & BVA** | **29** | **25** | **4** | **86.2%** |

---

## Detail Temuan Cacat Sistem (Defects Log)

### 1. BP04: Batas Karakter Maksimum Nama Lengkap (> 50 Karakter) Tidak Berfungsi
- Modul: Registrasi Akun Pengguna
- Severity: Medium \| Priority: Medium
- Deskripsi Masalah: Sesuai kebutuhan spesifikasi, field Nama Lengkap memiliki batas atas 50 karakter. Namun, saat diuji dengan input string sepanjang 51 karakter atau lebih, sistem tidak membatasi input atau menampilkan pesan kesalahan *"Nama maksimal 50 karakter"*, melainkan tetap memproses data tersebut.
- Rekomendasi Tindakan:
  - Tambahkan atribut `maxlength="50"` pada tag HTML `<input>` di antarmuka frontend.
  - Terapkan validasi form backend: `Rule::max(50)` atau anotasi `[StringLength(50)]` sebelum menyimpan record ke database MySQL.

---

### 2. BP10: Batas Karakter Maksimum Password (> 16 Karakter) Tidak Dibatasi
- Modul: Registrasi Akun Pengguna
- Severity: Medium \| Priority: Medium
- Deskripsi Masalah: Field kata sandi dirancang dengan rentang panjang 8 hingga 16 karakter. Pengujian nilai batas atas (`> 16` karakter) menunjukkan sistem tetap meloloskan kata sandi tanpa menampilkan peringatan *"Kata sandi maksimal 16 karakter"*.
- Rekomendasi Tindakan:
  - Terapkan validasi sanitasi panjang string password di form register.

---

### 3. AP12: Field Nomor Handphone Orang Tua Menerima Masukan Teks Huruf
- Modul: Pendaftaran Santri Baru
- Severity: Major \| Priority: High
- Deskripsi Masalah: Ketika field nomor telepon diisi dengan teks alfabet atau karakter non-angka, sistem seharusnya membatalkan pengiriman formulir dengan pesan *"Nomor harus berisi angka"*. Namun pada hasil pengamatan aktual, sistem tetap mengizinkan formulir tersimpan dan mengarahkan pengguna ke halaman invoice pembayaran. Kondisi ini berisiko menyebabkan kegagalan pengiriman notifikasi WhatsApp / SMS kepada wali santri.
- Rekomendasi Tindakan:
  - Ubah tipe input form menjadi `type="tel"`.
  - Terapkan pola regex validasi nomor telepon Indonesia: `pattern="^(08|\+628)[0-9]{8,12}$"`.
  - Tambahkan validasi sisi server sebelum melakukan insert query.

---

## Kesimpulan Evaluasi Kualitas Perangkat Lunak

1. Efektivitas Kombinasi EP & BVA: Penerapan Equivalence Partitioning dan Boundary Value Analysis terbukti sangat komplementer dalam mendeteksi kesalahan batas input numerik dan teks tanpa tumpang tindih (*zero redundancy*).
2. Kesiapan Operasional: Dengan tingkat kesesuaian fungsional mencapai 86%, sistem telah stabil untuk menangani alur bisnis pendaftaran dan autentikasi dasar, dengan catatan tim pengembang perlu segera menerapkan *patching* validasi batas atas dan sanitasi tipe data numerik sebelum rilis produksi penuh.
