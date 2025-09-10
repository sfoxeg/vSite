# CatchMe
Сервис для случки настенных ползунков

## Установка
```shell
git clone https://github.com/sfoxeg/vSite.git
```

```shell
cd vSite
```
```shell
pip install -r requirements.txt
```
```shell
py manage.py makemigrations
```
```shell
py manage.py migrate
```
```shell
py manage.py load_data
```

Опционально можно добавить тестовых админов
```shell
py manage.py create_users
```
