pip3 install -4 deps.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate