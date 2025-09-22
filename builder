if [ ! -f /app/db.sqlite3 ]; then
    python manage.py makemigrations main user search
    python manage.py migrate
    python manage.py create_users
    mkdir static/users_images
    python manage.py fake_data -c 25
else
  python manage.py migrate
fi

touch /tmp/flag
echo "Builder is done."
sleep 15