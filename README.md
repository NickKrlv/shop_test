Порядок действий:

python.exe -m pip install --upgrade pip
pip install -r reqiurements.txt

заглянуть в env.sample
создать свою базу данных

python manage.py makemigrations
python manage.py migrate

python manage.py load_data     # для выгрузки тестовых экземпляров моделей базы данных
python manage.py createsuperuser

python manage.py runserver

тестирование можно проводить в http://localhost:8000/swagger/
