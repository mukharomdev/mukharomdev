# Local
Untuk generate static file html di local computer :

```sh
make -C docs html
```

sedangkan untuk running lewat browser ada beberapa cara :

### python server
```sh
virtualenv .env
. .env/bin/activate
pyhton3 -m http.server -d docs/_build/html
```
- default port : 8000

atau,menggunakan php server ;

### php server

```
php -S localhost:8080 -t docs/_build/html

```