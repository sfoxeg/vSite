del db.sqlite3
rd /s/q user\migrations
py manage.py makemigrations main user search
py manage.py migrate
py manage.py create_users

mkdir static\users_images
py manage.py fake_data -c 200
