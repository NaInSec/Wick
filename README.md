### Wick

Ini adalah skrip Python yang digunakan untuk menghasilkan semua kemungkinan kombinasi kata sandi untuk Crack WAP dan file login atau kata sandi lainnya. Program ini adalah open source. Jika Anda melihat kebutuhan untuk memperbaiki atau mengubah sesuatu dengan segala cara, lakukanlah, tetapi bagikan temuan Anda. itu hanya benar.

Pemakaian : ```wick.py [-h] [-o OUTPUT] [-min MIN_SIZE] [-max MAX_SIZE] [-N] [-L] [-U] [-S] [-A] [-v]```

Menghasilkan daftar kata dengan semua kemungkinan kombinasi huruf termasuk :

```
-L (Lowercase Letters)
-U (Uppercase Letters)
-N (Numbers)
-S (Special Characters)
-A (All Characters, Numbers, and Letters)

-min (Minimum Size)
-max (Maximum Size)

-o outputfile.gz
or
-o stdout
```

Secara default -o filename.gz untuk membuat file teks terkompresi GZ dari semua kata. Gunakan kata kunci "stdout" untuk mencetak ke layar atau digunakan dengan program lain seperti aircrack-ng atau medusa.

```
./wick.py | xargs -L 1 medusa -h 192.168.1.1 -u admin -M web-form -p

./wick.py -o stdout -A | aircrack-ng -b XX:XX:XX:XX:XX:XX -w - file.cap
```
