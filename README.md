# CatchMe
Сервис для случки настенных ползунков

## Установка
```shell
git clone https://github.com/sfoxeg/vSite.git
cd vSite
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py load_data
```

Опционально можно добавить тестовых админов
```shell
py manage.py create_users
```
И произвольное число тестовых пользователей
```shell
py manage.py fake_data -c 100
```