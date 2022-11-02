# Tugas Kelompok Tengah Semester PBP - Mercatura
![deployment](https://github.com/AdrianRamadhan27/mercatura/actions/workflows/dpl.yml/badge.svg)

Nama anggota kelompok:
- Aidah Novallia Putri - 2106653400
- Katrina Gisella Sembiring - 2106707826
- Majid Rajendra Rahmat - 2106752382
- Raden Dhaneswara Timur Bhamakrti Rasendriya - 2106750710
- Raden Mohamad Adrian Ramadhan Hendar Wibawa - 2106750540

## Tautan Aplikasi
[Mercatura](https://mercatura-id.herokuapp.com)

## Latar belakang
Mengingat pentingnya digitalisasi untuk memulihkan perekonomian dunia, kelompok kami memutuskan untuk membuat suatu aplikasi yang dapat membantu setiap pelaku UMKM, khususnya UMKM dalam negeri, untuk mengembangkan bisnis mereka. Seperti yang kita tahu, bahwa sekitar 70% dari setiap bisnis UMKM sendiri memberikan potensi yang sangat besar untuk roda ekonomi negara Indonesia. Bukti ini dapat terlihat selama beberapa tahun terakhir yang dipaparkan dalam forum diskusi sekretariat presiden bahwa terbukti bahwa UMKM dapat meningkatkan Produk Domestik Bruto (PDB) negara sebanyak dua kali lipat atau lebih tepatnya 61,97%. Ditambah lagi, dengan data yang mengatakan bahwa UMKM menyerap tenaga kerja sebanyak 70% memberikan secercah harapan untuk mereduksi pengangguran yang kian marak di Indonesia. Bila ditarik dalam sebuah kesimpulan, Indonesia memiliki peluang yang cukup besar sebagai pemain aktif di pasar global. Sangat disayangkan sekali apabila produk-produk lokal yang terdapat dalam negara Indonesia tidak dapat dipromosikan ke dalam kancah internasional. Oleh karena itu, kami berharap dengan aplikasi ini, setiap UMKM memiliki kans yang lebih tinggi  untuk bersaing di pasar global. 


## Modul yang Diimplementasikan

### Login Module (Raden Dhaneswara Timur Bhamakrti Rasendriya)

- Halaman login

User yang telah mendaftarkan akun dapat memasukkan username dan password untuk masuk ke halaman website.
- Halaman registrasi akun


Pada halaman ini, pengguna baru atau Guest dapat mendaftarkan akun agar bisa login sebagai User.
- Halaman FAQ

Halaman ini berisi jawaban dari pertanyaan-pertanyaan yang umum ditanyakan pengguna Mercatura

### Main Page & Web Review Module (Majid Rajendra Rahmat)
- Halaman utama Mercatura

Halaman ini berisi kisah inspiratif dari beberapa usaha secara singkat. User ataupun Guest dapat menceritakan kisahnya dan akan ditampilkan disini.

- Halaman detail UMKM dan review website UMKM

Halaman ini berisi detail rinci tentang UMKM. User dapat memberikan penilaian terhadap usaha tersebut. Penilaian akan menyimpan nilai dari 1-5, deskripsi penilaian, pemberi nilai, dan tanggal dinilai.


### Article Module (Aidah Novallia Putri)

- Halaman kumpulan artikel

Halaman ini berisi daftar artikel seputar UMKM yang dibuat oleh user Mercatura.


- Halaman tambah artikel

User dapat mengunggah artikel yaitu dengan mengisi judul, tautan gambar, dan isi artikel. Sebuah artikel akan menyimpan username penulis, tanggal  diunggah, judul, gambar, dan isi.

- Halaman riwayat artikel

Halaman ini berisi daftar artikel yang telah dibuat oleh user tertentu yang login pada saat itu. Apabila user tersebut belum pernah membuat artikel, maka list artikel kosong.

### Kritik dan Saran Module (Katrina Gisella Sembiring)
- Halaman membuat kritik dan saran

Halaman ini berisi kritik dan saran yang User ingin sampaikan terkait dengan Mercatura. User juga dapat menyatakan bahwa ia setuju dengan kritik atau saran yang sudah dibaut sebelumnya dengan menekan tombol "Setuju". Membuat serta setuju dengan kritik dan saran hanya dibatasi untuk User yang sudah _log in_ saja, dan User yang tidak _log in_ hanya dapat melihat kritik dan saran yang sudah dibuat oleh User lain. 

### UMKM Module (Raden Mohamad Adrian Ramadhan Hendar Wibawa)
- Halaman daftar UMKM

Halaman ini berisi daftar nama UMKM. Terdapat searchbox yang memungkinkan pengguna untuk mencari UMKM berdasarkan keyword ataupun filter berdasarkan bidang dan lokasi usaha. 

- Halaman tambah UMKM

User dapat mendaftarkan UMKM yang dimilikinya. Sebuah data UMKM akan menyimpan nama usaha, bidang usaha, deskripsi usaha, kontak usaha, dan lokasi usaha, dan tautan ke website usaha jika ada.




### User Roles
- Guest: Pengguna yang belum mendaftarkan akun dapat mengakses seluruh website, tetapi tidak dapat membuat artikel baru, mengomentari artikel, atau menambahkan UMKM baru.
- User: Pengguna yang telah mendaftarkan akun dan masuk dengan username yang unik dan sebuah password. Dapat mengakses seluruh website dan dapat menggunakan semua fitur yang ada.

