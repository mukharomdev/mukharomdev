# Local computer
		...pastikan sudah terinstall :
- Python3
- pip3
- virtualenv

## setup environment
```sh
virtualenv .env
. .env/bin/activate
pip3 install -r requirements.txt
```
Untuk generate static file html di local computer :
```sh
make -C docs html
```

...,sedangkan untuk running lewat browser ada beberapa cara :

### python server
```sh
virtualenv .env
. .env/bin/activate
pyhton3 -m http.server -d docs/_build/html 8000
```
- default port : 8000
- jika port 8000 tidak bisa ,ganti 8001 atau 8081 etc

atau,menggunakan php server ;

### php server

```
php -S localhost:8080 -t docs/_build/html

```

## Check broken link
 ...Perintah dibawah ini adalah untuk mengecek status website link masih aktif atau tidak.Jadi,pastikan ada koneksi internet yang tersambung ke komputer.Proses yang terjadi memakan waktu yang relatif lama tergantung kondisi tertentu.

```sh
make -C docs linkcheck
```