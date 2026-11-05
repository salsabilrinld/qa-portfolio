# 🔌 API & GraphQL Test Cases: LMS Tutoring Academy

Dokumentasi pengujian antarmuka pemrograman aplikasi (API Testing) pada backend **ASP.NET Core** menggunakan **GraphQL (Hot Chocolate)** dan REST Auth Endpoint.

---

## 📌 Ringkasan Arsitektur API

| Komponen | Spesifikasi |
|---|---|
| **Teknologi Backend** | ASP.NET Core Web API |
| **Query Engine** | GraphQL (Hot Chocolate Server) |
| **Endpoint GraphQL** | `POST /graphql` |
| **Format Data** | JSON Payload |
| **Mekanisme Autentikasi** | Bearer Token (JSON Web Token / JWT) |
| **Tool Pengujian** | Postman, Banana Cake Pop (GraphQL IDE), cURL |

---

## 1. GraphQL Mutation: `registerStudent` (Autentikasi Registrasi)

### Query / Mutation Payload
```graphql
mutation RegisterStudent($input: RegisterStudentInput!) {
  registerStudent(input: $input) {
    student {
      id
      fullName
      email
      status
    }
    errors {
      code
      message
    }
  }
}
```

### Variabel Input Valid
```json
{
  "input": {
    "fullName": "Elysian",
    "email": "elysian@student.lms.com",
    "password": "Elysian123!"
  }
}
```

### Matriks Pengujian API Registrasi

| API Test ID | Skenario Pengujian | Input Data Kondisi | Expected Status Code | Expected JSON Response | Kesimpulan |
|---|---|---|---|---|---|
| **API-REG-01** | Registrasi akun siswa baru dengan payload valid | Data nama lengkap, email valid, dan password kuat | `200 OK` | `data.registerStudent.student.id != null` dan `errors: null` | ✅ **Pass** |
| **API-REG-02** | Registrasi dengan email yang sudah terdaftar (*Duplicate Key*) | Email: `budi@email.com` (terdaftar di database) | `200 OK` (GraphQL Error) | `errors[0].code: "DUPLICATE_EMAIL"` | ✅ **Pass** |
| **API-REG-03** | Registrasi dengan format email salah (*Missing Domain*) | Email: `elysianemail.com` | `400 Bad Request` | `errors[0].message: "Invalid email format"` | ✅ **Pass** |
| **API-REG-04** | Registrasi dengan password di bawah 8 karakter | Password: `short` | `400 Bad Request` | `errors[0].message: "Password minimum 8 characters"` | ✅ **Pass** |

---

## 2. GraphQL Mutation: `loginUser` (Autentikasi Multi-Role)

### Query / Mutation Payload
```graphql
mutation LoginUser($input: LoginInput!) {
  loginUser(input: $input) {
    token
    role
    user {
      id
      email
    }
    message
  }
}
```

### Matriks Pengujian API Login

| API Test ID | Skenario Pengujian | Input Payload | Expected Status Code | Expected JSON Response | Kesimpulan |
|---|---|---|---|---|---|
| **API-AUTH-01** | Login peran Admin dengan kredensial valid | `{"email": "admin@lms.com", "password": "admin123"}` | `200 OK` | Mengembalikan JWT token valid & `role: "ADMIN"` | ✅ **Pass** |
| **API-AUTH-02** | Login peran Siswa dengan kredensial valid | `{"email": "siswa@lms.com", "password": "siswa123"}` | `200 OK` | Mengembalikan JWT token valid & `role: "STUDENT"` | ✅ **Pass** |
| **API-AUTH-03** | Login dengan kata sandi keliru | `{"email": "admin@lms.com", "password": "WrongPassword!"}` | `401 Unauthorized` | `message: "Kredensial tidak cocok"` | ✅ **Pass** |
| **API-AUTH-04** | Login akun dengan status `inactive` / `suspended` | Akun nonaktif | `403 Forbidden` | `message: "Akun Anda dinonaktifkan oleh administrator"` | ✅ **Pass** |

---

## 3. GraphQL Query: `getCourseModules` (Akses Konten Pembelajaran)

### Query Payload
```graphql
query GetCourseModules($courseId: ID!) {
  course(id: $courseId) {
    id
    title
    modules {
      id
      title
      videoUrl
      duration
      isLocked
    }
  }
}
```

### Matriks Pengujian API Konten

| API Test ID | Skenario Pengujian | Header Otorisasi | Expected Result | Kesimpulan |
|---|---|---|---|---|
| **API-MOD-01** | Siswa terdaftar mengakses materi kelas aktif | `Authorization: Bearer <valid_student_token>` | Seluruh modul terbuka (`isLocked: false`) | ✅ **Pass** |
| **API-MOD-02** | Pengguna guest/tanpa login mengakses URL video | *Tanpa Header Authorization* | Endpoint mengembalikan error 401 dan konten terenkripsi/terkunci | ✅ **Pass** |
| **API-MOD-03** | Siswa mengakses kelas berbayar yang belum dibeli | `Authorization: Bearer <valid_unpaid_token>` | Respon menampilkan metadata judul namun `videoUrl: null` dan `isLocked: true` | ✅ **Pass** |
