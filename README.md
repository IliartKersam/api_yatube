# Yatube project API

### Description:
API for social network, write posts, attach pictures, leave comments, subscribe to any authors.
### Technologies
- Python 3.7
- Django 2.2.19
- Django REST framework

### How to start the project:
Clone repository and go to it's derictory on your computer:

```
git clone https://github.com/IliartKersam/api_final_yatube.git
```

```
cd yatube_api
```

Create and activate virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Change directory and make migrations:
```
cd yatube_api
```

```
python manage.py migrate
```

Run project:

```
python manage.py runserver
```
### API documentation
Documentation for the Yatube API is available at: /redoc/
### Author
Kashtanov Nikolay

Kazan, 2022
