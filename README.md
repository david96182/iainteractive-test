## Iainteractive-test



---

### Requirements

- Python >= 3.10
- Mysql
- Django
- Django Rest Framework
- drf-yasg

### Set Up Project

Clone this repository

```git
git clone https://github.com/david96182/iainteractive-test.git
```

Go to the project folder

```bash
cd iainteractive-test
```

Create a python virtual environment

```bash
python -m venv venv
```

Activate Python environment

```bash
. venv/bin/activate
```

Install Python Requirements

```bash
pip install -r requirements.txt
```

Create project database

- Install mysql if not installed

- Enter interactive bash with your user: 

  ```bash
  mysql -u USER -p
  ```

- Create database:

  ```mysql
  CREATE DATABASE mageacademy CHARACTER SET utf8;
  ```

Update database settings:

- Create file my.cnf
- Update the file with your settings

Run migrations to load database scheme:

```bash
python manage.py migrate
```

Create Admin superuser

```bash
python manage.py createsuperuser
```

Run seed

```bash
python manage.py loaddata academyapi/seed/grimoire.json
```

```bash
python manage.py loaddata academyapi/seed/magicaffinity.json
```

Or using bash script can run migrate and seed:

```bash
sh migrate_and_seed.sh
```

Run server

```bash
python manage.py runserver
```

You can access admin panel with your credentials:

- Go to http://localhost:8000/admin/

You can check API specifications in:

- Go to http://localhost:8000/swagger/

