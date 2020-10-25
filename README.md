django-admin startproject school
python manage.py startapp library

sudo docker run --name postgres_library -d -p 5432:5432 -e POSTGRES_USER=nik -e POSTGRES_PASSWORD=nikgreat -e POSTGRES_DB=library postgres
docker start postgres_library

python3 manage.py makemigrations
python3 manage.py makemigrations covid
python3 manage.py migrate
python3 manage.py runserver
