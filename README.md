## Membuat aplikasi NEWS MAGAZINE menggunakan Framework Django versi 2.2.5

[Github repo](https://github.com/gurnitha/django-news-magazine)
[My Learning](https://www.udemy.com/course/python-django-tkinter-complete-bundle-advance/learn/lecture/16516178#overview)


## Section 0: Github

        Aktivitas:

        1. Modifikasi file README.md
        modified:   .gitignore
        modified:   README.md


#### 0.1 Create a new repository

        Aktivitas:

        1. Membuat repositori baru di Github

        NEXT:

        Clone repositori 


#### 0.2 Clone the repositori

        Aktivitas:

        1. Clone the repositori

        NEXT:

        2. Setup


## Section 1: Setup

        Aktivitas:

        1. Modidikasi file README.md 

        NEXT:

        1.1 Instal requirements


#### 1.1 Instal requirements

        Aktivitas:

        1. Instal:

        - Node.js
        - Python
        - Pip
        - Viertualenv 

        NEXT:

        Section 2: Create proyek django


## Section 2: Run your first website

        Aktivitas:

        1. Modidikasi file README.md 

        NEXT:

        2.1 Create django project


#### 2.1 Create django project

        Aktivitas:

        1. Create django project

        (venv39322) λ django-admin startproject newsmag .

        2. Run the server

        (venv39322) λ python manage.py runserver

        modified:   README.md
        new file:   manage.py
        new file:   newsmag/__init__.py
        new file:   newsmag/asgi.py
        new file:   newsmag/settings.py
        new file:   newsmag/urls.py
        new file:   newsmag/wsgi.py

        NEXT:

        2.2 Django settings


#### 2.2 Django settings

        Aktivitas:

        1. Set static file and timezone
        modified:   newsmag/settings.py

        NEXT:

        2.3 Django Urls


#### 2.3 Django Urls and import os

        Aktivitas:

        1. Import os
        modified:   newsmag/settings.py
        
        2. Modified the url
        modified:   newsmag/urls.py

        NEXT:

        2.4 Default Django Admin


#### 2.4 Default Django Admin

        Aktivitas:

        1. Create superuser

        NEXT:

        3. Create django app


## Secion 3: Create django app

        Aktivitas:

        1. Modidikasi file README.md 

        NEXT:

        3.1 Create 'main' app


#### 3.1 Create a new app - Part 1: called it 'main'

        Aktivitas:

        1. Create a new app
        (venv39322) λ mkdir app
        (venv39322) λ mkdir app\main
        (venv39322) λ django-admin startapp main app\main

        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

        NEXT:

        3.1 Create a new app - Part 2: register it to the config/settings.py


#### 3.1 Create a new app - Part 2: register it to the config/settings.py

        Aktivitas:

        1. Mengubah file apps.py yang ada di dalam app/main
        
        from: name = 'main'
        to: name = 'app.main'        

        2. Registrasi 'main' app pada newsmag/settings.py
        modified:   newsmag/settings.py

        3. Testing: run the server :)

        NEXT:

        3.2 App settings


#### 3.2 App settings

        Aktivitas:

        1. Membuat file baru: main/urls.py

        2. Membuat path pada main/urls.py

        3. Menyertakan (include) path dari main app pada path dari newsmag

        4. Membuat folder static dan templates

        5. Testing: jalankan server

        6. Result: berhasil

        7. Daftar file yang berubah/baru

        modified:   README.md
        new file:   app/main/urls.py
        modified:   newsmag/urls.py

        NEXT:

        3.3 App layer


#### 3.3 App layer

        Aktivitas:

        1. Membuat contoh model dengan nama 'Main'

        2. Membuat contoh home_page views

        3. Tesing: jalankan server

        4. Result: berhasil

        5. Daftar file/folder yang berubah/baru

        modified:   README.md
        modified:   app/main/models.py
        modified:   app/main/views.py

        NEXT:

        3.4 Test app


#### 3.4 Test app

        Aktivitas:

        1. Membuat folder dan file baru:
           templates/app/main/home_page.html + teks

        2. Mendefinisikan path untuk home page pada app/main/urls.py

        3. Mengaktifkan django templates pada newsmag/settings.py

        4. Testing: jalankan server buka http://127.0.0.1:8000/

        5. Result: berhasil

        6. Daftar file/folder yang berubah/baru
        
        modified:   README.md
        modified:   app/main/urls.py
        modified:   newsmag/settings.py
        new file:   templates/app/main/home_page.html

        NEXT:

        3.5 Aktifkan django admin


#### 3.5 Aktifkan django admin

        Aktivitas:

        1. Register Main model 

        2. Jalankan migrasi

        3. Testing:

        3.1 Login ke admin
        3.2 Add test
        3.3 Save

        4. Result: berhasil 

        5. Daftar file/folder yang berubah/baru

        modified:   README.md
        modified:   app/main/admin.py
        new file:   app/main/migrations/0001_initial.py
        NEXT:

        Section 4: Django Bootstrap