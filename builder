python manage.py makemigrations main user search
python manage.py migrate
python manage.py create_users

mkdir static/users_images
python manage.py fake_data -c 20

touch /tmp/flag
echo "Builder is done."
sleep 15