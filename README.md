# API проекта Yatube

### Описание проекта:
Социальная сеть, пишите посты, прикрепляйте картинки, оставляйте комментарии, подписывайтесь на любымих авторов!

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IliartKersam/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры
Документация для API Yatube доступна по ссылке: http://127.0.0.1:8000/redoc/
