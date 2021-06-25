## MEMBUAT APLIKASI FORUM MENGGUNAKAN DJANGO DAN POSTGRESQL

#### 1. Membuat remote repositori pada Github 

        ing@DESKTOP-5NU2HDJ:/mnt/e/workspace/django/Italian/DjangoForum$ tree -L 1
        .
        └── readme.md        
        new file:   .gitignore
        new file:   readme.md

#### 2. Membuat virtual environment

        E:\workspace\django\Italian\DjangoForum (main)
        λ python -m venv venv3921
        modified:   .gitignore
        modified:   readme.md

#### 3. Menginstal Django v2.1        

        E:\workspace\django\Italian\DjangoForum (main)
        (venv3921) λ python -m pip install django==2.1
        modified:   readme.md

#### 3. Membuat Django Proyek 'DjangoForum/config'

        .
        ├── config
        │ 	├── __init__.py
        │ 	├── settings.py
        │ 	├── urls.py
        │ 	└── wsgi.py
        ├── manage.py
        ├── readme.md
        └── venv3921
            ├── Include
            ├── Lib
            ├── Scripts
            └── pyvenv.cfg

#### 4. Database Part 1: Membuat Postgres database

        hp=# CREATE DATABASE django_forum_italian;  

#### 5. Database Part 2: Instal packages django-environ dan postgres driver

        (venv3921) λ pip install psycopg2 
        (venv3921) λ pip install django-environ

#### 6. Database Part 3: Menambahkan django-environ pd settings.py

        modified:   config/settings.py
        modified:   readme.md 

#### 7. Database Part 4: Membuat .env file di dalam config 

        modified:   .gitignore
        modified:   readme.md












































































































































