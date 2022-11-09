What This Is
------------

My first take at Django. Hope this came out well!

This project is supposed to be run along with a celery worker to allow heavy api endpoints to be run off-thread.

To Install
----------

    git clone https://github.com/4310V343k/DjangoFirstProject
    cd DjangoFirstProject
    # create, activate venv, install deps
    python3 -m venv venv
    . venv/Scripts/activate
    pip install -r requirements.txt
    # run the server
    python manage.py runserver

To Set Up
---------

    . venv/Scripts/activate
    # create a user to be able to use endpoints not in ro mode
    python manage.py createsuperuser

To Run
------

**The App**

    . venv/Scripts/activate
    python manage.py runserver

**The Celery worker**

    . venv/Scripts/activate
    celery -A mangalib worker
    # if you're on windows use an alternative event pool
    celery -A mangalib worker -P solo

API Examples
-----------

**Create a new Title**

    http -a login:pass :8000/api/titles/ -- russian_name="Название"

**Get your newly created Title**

    http :8000/api/titles/1/

Django Admin
------------

You can also visit `http://127.0.0.1:8000` for an easier access to all the models.
