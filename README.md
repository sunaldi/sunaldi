# Sunaldi (SMANUAT United Alumni Directory)

[![Test and Deploy][actions-badge]][commits-gh]

Sunaldi (SMANUAT United Alumni Directory) adalah situs web yang menyediakan data alumni SMAN Unggul Aceh Timur untuk ditelusuri.

## Daftar Isi

- [Daftar Isi](#daftar-isi)
- [Tata Cara](#tata-cara)
- [Lisensi](#lisensi)
- [Referensi](#referensi)


## Tata Cara

Jika Anda adalah alumni SMAN Unggul Aceh Timur yang ingin berkontribusi dalam pembuatan situs web ini, berikut adalah langkah-langkah yang perlu dilakukan.

1. Pastikan Anda memiliki kompetensi di Python, Django, HTML, CSS, dan Bootstrap. Kemampuan dalam AJAX dan/atau Fetch API menjadi nilai tambahan.
2. Laporkan diri Anda ke [Muhammad Athallah][email-athal] untuk ditambahkan sebagai _maintainer_ dari Sunaldi.
3. Clone repo sunaldi ke _local workspace_ Anda dan buatlah branch baru dengan perintah `git checkout -b [NAMA_BRANCH]`.
4. Untuk memulai modul baru, gunakan perintah `python manage.py startapp [NAMA_MODUL]`.
5. Apabila Anda menambahkan atau mengubah model, jangan lupa lakukan `python manage.py makemigrations` dan `python manage.py migrate`.
6. Untuk menjalankan server di _local workspace_ Anda, gunakan perintah `python manage.py runserver`.
7. Untuk mengunggah hasil kerja Anda pada branch Anda, gunakan empat mantra ajaib Git: `git pull origin master`, `git add .`, `git commit -m [PESAN_ANDA]`, dan `git push origin [NAMA_BRANCH]`.
8. Untuk menerapkan hasil kerja Anda secara permanen, gunakan fitur **Pull Request** pada situs web repo. **<u>Jangan pernah mengunggah hasil kerja Anda secara langsung ke branch main.</u>**
9. Apabila terdapat pertanyaan, kritik, ataupun saran, silakan kontak Athal melalui [surat elektroniknya][email-athal].


## Lisensi

Kode sumber situs web ini memiliki lisensi [AGPL-3.0 License][license].


## Referensi

Berikut ini adalah sumber referensi yang digunakan dalam pembuatan situs web ini.
- [django-template-heroku][project-template]
- [Zinc - Free Bootstrap 5 HTML5 Business Website Template][web-template]
- [Beautiful Free Images & Pictures | Unsplash][unsplash]

[actions-badge]: https://github.com/sunaldi/sunaldi/workflows/Test%20and%20Deploy/badge.svg
[commits-gh]: https://github.com/sunaldi/sunaldi/commits/master
[email-athal]: mailto:mhd.athallah@gmail.com
[license]: LICENSE
[project-template]: https://github.com/laymonage/django-template-heroku/
[web-template]: https://themewagon.com/themes/free-bootstrap-5-html5-business-website-template-zinc/
[unsplash]: https://unsplash.com