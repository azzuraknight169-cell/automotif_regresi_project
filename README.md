# Proyek Regresi Linear - Otomotif

**Mahasiswa:** Bayu Muhammad Ramadhan  
**NIM:** 301240008  
**Kelas:** 5A  
**Mata kuliah:** Pembelajaran Mesin

## Judul
Analisis Pengaruh Kapasitas Mesin terhadap Efisiensi Bahan Bakar Mobil Menggunakan Regresi Linear Sederhana.

## Studi kasus
- Variabel input (X): `displ` = kapasitas mesin dalam liter.
- Variabel target (y): `hwy` = efisiensi bahan bakar jalan raya, dalam miles per gallon (MPG).
- Dataset: 234 baris dan 11 kolom, subset data EPA untuk mobil tahun 1999 dan 2008.
- Sumber dataset: https://plotnine.org/reference/mpg.html

## Menjalankan aplikasi di komputer lokal
1. Pasang Python 3.10 atau lebih baru.
2. Buka terminal pada folder proyek ini.
3. Buat virtual environment (disarankan): `python -m venv .venv` lalu aktifkan.
4. Instal pustaka: `pip install -r requirements.txt`.
5. Latih model dan simpan file model: `python train_model.py`.
6. Jalankan web: `python app.py`.
7. Buka `http://127.0.0.1:5000` di browser.

## Evaluasi hasil model
Pembagian data memakai `test_size=0.20` dan `random_state=42`. Script `train_model.py` melaporkan R-squared, MAE, dan RMSE. Hasil validasi saat disusun:
- Intersep: 36.1620
- Koefisien `displ`: -3.6528
- R-squared: 0.5275
- RMSE: 3.5391 MPG
- MAE: 2.4844 MPG

## Struktur berkas
- `app.py`: server Flask dan endpoint prediksi.
- `templates/index.html`: antarmuka pengguna.
- `train_model.py`: preprocessing, pelatihan, evaluasi, dan penyimpanan model.
- `model.joblib`: model terlatih (dapat dibuat ulang dengan menjalankan `train_model.py`).
- `model_metrics.json`: metrik model.
- `mpg.csv`: dataset.
- `validasi_dataset.ipynb`: notebook untuk cek data dan visualisasi.
- `scatter_regresi.png` dan `aktual_vs_prediksi.png`: grafik analisis.
- `TP-02_301240008_Bayu_Muhammad_Ramadhan.docx/.pdf`: laporan tugas pendahuluan jika ikut dimasukkan ke paket.
- `TA-02_301240008_Bayu_Muhammad_Ramadhan.docx/.pdf`: laporan tugas akhir jika ikut dimasukkan ke paket.

## Deployment ke Railway melalui GitHub

1. Pastikan berkas proyek (`app.py`, `requirements.txt`, `Procfile`, `mpg.csv`, `model.joblib`, `train_model.py`, dan folder `templates/`) berada langsung di root repositori GitHub.
2. Buat repositori GitHub, lalu push isi folder proyek ini. Jangan mengunggah folder virtual environment `.venv/`.
3. Di Railway, pilih **New Project** → **Deploy from GitHub repo**, lalu pilih repositori proyek ini dan izinkan akses GitHub jika diminta.
4. Railway mendeteksi proyek Python dari `requirements.txt`. Pada pengaturan service, isi **Start Command** dengan:

   `python train_model.py && gunicorn --bind 0.0.0.0:$PORT app:app`

   Perintah ini melatih ulang dan menyimpan model sesuai versi pustaka di deployment, kemudian menjalankan Flask melalui Gunicorn pada port yang diberikan Railway.
5. Mulai/redeploy service dan periksa **Deploy Logs** sampai proses berhasil.
6. Buka **Settings** → **Networking** lalu pilih **Generate Domain** untuk membuat URL publik. Uji aplikasi dengan kapasitas mesin, misalnya `2.0` liter.

Tidak ada environment variable rahasia yang diperlukan oleh aplikasi ini. Jangan membuat variabel `PORT` sendiri kecuali ada alasan khusus; gunakan port yang disediakan Railway.

## Tautan eksternal yang perlu dilengkapi sebelum pengumpulan
- GitHub: [isi setelah repositori dibuat dan diunggah]
- Aplikasi Railway: [isi setelah deployment berhasil]
- Video YouTube: [isi setelah merekam dan mengunggah presentasi]

Jangan menuliskan tautan palsu. Pastikan aplikasi berhasil dijalankan dan URL publik benar-benar aktif sebelum menyerahkan laporan final.

## Tautan eksternal yang perlu dilengkapi sebelum pengumpulan
- GitHub: [isi setelah repositori dibuat dan diunggah]
- Aplikasi Render: [isi setelah deployment berhasil]
- Video YouTube: [isi setelah merekam dan mengunggah presentasi]

Jangan menuliskan tautan palsu. Pastikan aplikasi berhasil dijalankan dan URL publik benar-benar aktif sebelum menyerahkan laporan final.

## Referensi
1. plotnine. (n.d.). *mpg*. https://plotnine.org/reference/mpg.html
2. Wickham, H., & Grolemund, G. *Fuel economy data*. https://ggplot2-book.org/getting-started.html
3. Scikit-learn. *LinearRegression*. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
