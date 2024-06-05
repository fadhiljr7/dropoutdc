# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Institut adalah pendidikan tinggi berkualitas dengan tujuan mencetak lulusan yang kompeten dan berkualitas. Institusi ini telah membangun reputasi yang sangat baik dalam mencetak lulusan yang sukses. Namun, tantangan yang dihadapi adalah tingkat dropout siswa yang tinggi. Dropout ini merupakan masalah serius yang dapat mengurangi reputasi institusi dan juga berdampak negatif pada kesuksesan siswa.

Untuk mengatasi masalah ini, Jaya Institut ingin mengambil langkah proaktif dengan menggunakan data dashboard dan solusi machine learning. Mereka ingin mendeteksi siswa yang mungkin akan melakukan dropout secepat mungkin agar dapat memberikan bimbingan dan dukungan khusus kepada mereka. Dengan demikian, institusi tersebut berharap dapat meningkatkan tingkat retensi siswa dan menciptakan lingkungan pendidikan yang mendukung bagi semua siswa untuk menyelesaikan pendidikan mereka dengan sukses.

### Permasalahan Bisnis
- Tingkat Dropout yang Tinggi: Institusi pendidikan menghadapi tantangan besar dalam hal tingkat dropout siswa yang tinggi, yang dapat mengurangi reputasi institusi dan menghambat kesuksesan siswa.
- Kesulitan Mendeteksi Siswa yang Berpotensi Dropout: Identifikasi siswa yang berisiko tinggi untuk melakukan dropout sebelumnya merupakan tantangan, karena seringkali tanda-tanda awal tidak terdeteksi secara tepat waktu.
- Kurangnya Intervensi yang Tepat: Tanpa adanya informasi yang akurat tentang siswa yang berpotensi dropout, institusi kesulitan memberikan bimbingan dan dukungan khusus kepada mereka untuk mencegah keluar dari pendidikan.
- Pengambilan Keputusan yang Terbantu oleh Data: Kurangnya alat yang dapat membantu pengambil keputusan di institusi pendidikan untuk mengidentifikasi pola dan faktor-faktor yang mempengaruhi tingkat keluar siswa serta mengambil tindakan yang tepat untuk meningkatkan retensi siswa.

### Cakupan Proyek
Pengembangan Data Dashboard:
- Desain dan implementasi dashboard interaktif yang menyajikan informasi tentang tingkat dropout siswa berdasarkan berbagai faktor seperti kursus, status perkawinan, status penerima beasiswa, dan kehadiran siswa.
- Integrasi data dari berbagai sumber untuk memungkinkan visualisasi yang komprehensif dan akurat.
- Pembuatan fitur-fitur seperti grafik tren, pembandingan antar kelompok, dan filter untuk memudahkan analisis.
Pengembangan Solusi Machine Learning:
- Pengumpulan dan pembersihan data yang diperlukan untuk pelatihan model machine learning, termasuk dropout historis siswa dan atribut-atribut yang relevan.
- Pelatihan model machine learning untuk memprediksi kemungkinan siswa melakukan dropout berdasarkan faktor-faktor yang ada.
- Integrasi model ke dalam sistem institusi pendidikan sehingga dapat digunakan untuk memberikan rekomendasi dan intervensi kepada siswa yang berisiko tinggi.

### Persiapan

Sumber data: drop_out.csv

Setup environment:
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard yang telah dibuat adalah sebuah alat yang memungkinkan manajemen Jaya Institut untuk memantau dan menganalisis tingkat dropout siswa secara komprehensif. Dashboard ini menyajikan data tentang tingkat dropout siswa berdasarkan beberapa faktor yang relevan termasuk course, status perkawinan, status penerima beasiswa, dan kehadiran siswa. Dengan menggunakan visualisasi yang intuitif seperti grafik dan diagram, dashboard ini memberikan wawasan yang berharga tentang tren dan pola tingkat dropout dari waktu ke waktu serta perbandingan antara kelompok siswa yang berbeda. Manajemen dapat dengan cepat mengidentifikasi area-area di mana tingkat dropout paling tinggi, sehingga mereka dapat mengambil tindakan yang tepat untuk meningkatkan retensi siswa. Selain itu, dashboard ini juga memungkinkan pengguna untuk melakukan analisis lebih mendalam dengan memberikan filter dan fitur interaktif sehingga mereka dapat mengeksplorasi data sesuai dengan kebutuhan mereka. Dengan demikian, business dashboard ini menjadi alat yang sangat berharga bagi manajemen institusi untuk mengambil keputusan strategis dalam meningkatkan kualitas pendidikan dan mencapai tingkat kelulusan yang lebih tinggi.

Data Dashboar dapat diakses melalui link berikut: https://lookerstudio.google.com/reporting/e5539666-99de-4300-9f2f-f4c3cebacc9d

## Menjalankan Sistem Machine Learning
Persiapkan Data:
- Pastikan Anda memiliki file data yang sesuai dengan format yang diperlukan oleh sistem, dalam kasus ini, file selected_columns.csv.
Instalasi Library:
- Pastikan Anda telah menginstal semua library yang diperlukan seperti pandas, streamlit, dan scikit-learn.
Jalankan Kode:
- Jalankan file app.py menggunakan interpreter Python. Anda dapat melakukannya dengan mengetikkan python nama_file.py di terminal atau command prompt.
Interaksi dengan Aplikasi:
- Setelah menjalankan kode, sebuah aplikasi web akan terbuka di browser Anda.
- Pada sidebar aplikasi, Anda dapat memasukkan informasi siswa seperti status perkawinan, mode aplikasi, kursus, kehadiran, dan status penerima beasiswa.
- Setelah memasukkan informasi, aplikasi akan memberikan prediksi apakah siswa tersebut berpotensi dropout atau tidak, beserta dengan probabilitasnya.
```
pip install streamlit
pip install scikit-learn
streamlit run app.py
```
Sistem Machine Learning dapat diakses melalui link berikut: https://dropoutdc-kzhcafdes6vesfjc9xx3wz.streamlit.app/

## Conclusion
kesimpulan proyek data dashboard dan solusi machine learning adalah bahwa ada beberapa faktor yang berpotensi memengaruhi tingkat dropout siswa di institusi pendidikan. Dengan visualisasi dan analisis yang disediakan, kita dapat melihat bahwa tingkat keluar cenderung bervariasi berdasarkan course, status perkawinan, status penerima beasiswa atau scholarship, dan kehadiran siswa. Selain itu, dengan menggunakan model machine learning, kita dapat memprediksi tingkat dropout siswa dan mengidentifikasi siswa yang berisiko tinggi untuk keluar, memungkinkan lembaga pendidikan untuk melakukan intervensi yang tepat waktu dan meningkatkan retensi siswa secara keseluruhan. Kedua alat ini dapat memberikan wawasan yang berharga bagi pengambil keputusan di institusi pendidikan untuk meningkatkan kualitas pendidikan dan mencapai tingkat kelulusan yang lebih tinggi.

### Rekomendasi Action Items
- Implementasi Early Warning System: Perusahaan dapat mengimplementasikan sistem peringatan dini untuk mendeteksi siswa yang berpotensi dropout. Dengan mendeteksi siswa ini lebih awal, perusahaan dapat memberikan intervensi yang tepat waktu untuk mencegah dropout.
- Pengembangan Program Bimbingan dan Dukungan: Berdasarkan hasil prediksi dari solusi machine learning, perusahaan dapat mengembangkan program bimbingan dan dukungan khusus bagi siswa yang berisiko tinggi untuk melakukan dropout. Program ini dapat mencakup mentoring, konseling, dan dukungan akademis tambahan untuk membantu siswa mengatasi tantangan yang mereka hadapi.
- Analisis Faktor Penyebab Dropout: Melalui data dashboard, perusahaan dapat melakukan analisis mendalam terhadap faktor-faktor yang mempengaruhi tingkat dropout siswa. Dengan memahami penyebab dropout, perusahaan dapat mengidentifikasi pola atau tren yang mungkin terjadi dan mengembangkan strategi yang lebih efektif untuk meningkatkan retensi siswa.
- Peningkatan Keterlibatan Siswa: Perusahaan dapat mengadopsi strategi untuk meningkatkan keterlibatan siswa di dalam kelas dan di luar kelas. Ini dapat mencakup penggunaan teknologi pendidikan, program pengembangan keterampilan soft skill, dan kegiatan ekstrakurikuler yang menarik minat siswa.
- Kolaborasi dengan Pihak Eksternal: Perusahaan dapat menjalin kemitraan dengan lembaga atau organisasi eksternal seperti lembaga bimbingan karier, lembaga pemerintah, atau perusahaan swasta untuk menyediakan lebih banyak sumber daya dan dukungan bagi siswa.
