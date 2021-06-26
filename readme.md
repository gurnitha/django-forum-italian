## MEMBUAT APLIKASI FORUM MENGGUNAKAN DJANGO DAN POSTGRESQL


### 1. SETUP

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


### 2. DJANGO PROYEK

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


### 3. DATABASE

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

#### 8. Database Part 5: Menambahkan kredensial database pada .env file

        modified:   readme.md

#### 9. Database Part 6: Mengganti SECRET_KEY dan Database kredensial pada settings.py dgn db kredensial yg ada pada .env file

        modified:   config/settings.py
        modified:   readme.md

#### 10. Database Part 7: Jalankan server untuk menguji

        (venv3921) λ python manage.py runserver
        Performing system checks...

        System check identified no issues (0 silenced).
        June 25, 2021 - 20:51:56
        Django version 2.1, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


### 4. USER AUTHENTICATION

#### 11. User Authentication Part 1: Membuat app  di dalam foderl apps 'accounts'

        .
        ├── apps
        │	 └── accounts
        │	     ├── __init__.py
        │	     ├── admin.py
        │	     ├── apps.py
        │	     ├── migrations
        │	     ├── models.py
        │	     ├── tests.py
        │	     └── views.py
        ├── config
        ├── manage.py
        ├── readme.md
        └── venv3921

#### 12. User Authentication Part 2: Meregistrasi accounts app pada config/settings.py

        modified:   apps/accounts/apps.py
        modified:   config/settings.py
        modified:   readme.md

#### 13. User Authentication Part 3: Membuat form registrasi

        new file:   apps/accounts/forms.py
        modified:   readme.md

#### 14. User Authentication Part 4: Membuat view function untuk memvalidasi data user

        modified:   apps/accounts/views.py
        modified:   readme.md


#### 15. User Authentication Part 5: Membuat urls.py pada accounts 

        new file:   apps/accounts/urls.py
        modified:   readme.md


#### 15. User Authentication Part 6: Memasukan accounts/urls.py pada config/urls.py

        modified:   config/urls.py
        modified:   readme.md

#### 16. User Authentication Part 7: Memodifikasi LANGUAGE_CODE dan TIME_ZONE 

        modified:   config/settings.py
        modified:   readme.md


#### 17. User Authentication Part 8: Templates - setting up templates

        new file:   apps/accounts/templates/accounts/registrasi.html
        modified:   config/settings.py
        modified:   readme.md

#### 18. User Authentication Part 9: Templates -  install django_crispy_forms

        (venv3921) λ pip install django_crispy_forms
        modified:   readme.md

#### 19. User Authentication Part 10: Templates - Membuat base.html template

        modified:   readme.md
        new file:   templates/base.html

#### 20. User Authentication Part 11: Templates - Modifikasi registrasi form page dam regostrasi django-crispy

        modified:   apps/accounts/templates/accounts/registrasi.html
        modified:   config/settings.py
        modified:   readme.md


#### 20. User Authentication Part 11: Templates - Menambahkan bootstrap4 paket pada settings.py

        CRISPY_TEMPLATE_PACK = "bootstrap4" 






































































































