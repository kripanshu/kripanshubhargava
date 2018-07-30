# MyWebsite : kripanshubhargava
------
## Install

Prerequisites:
  - python3
  - [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)


Open a Terminal, from the top of this repository, run:

```
# from within ~/my_website 
mkvirtualenv mywebsite
pip install -r requirements/requirements.txt
```

------

## Run the website from python web server

Open a Terminal, from the top of this repository, run:

```
# from within ~/my_website
# ------------------------
workon mywebsite

# ------------------------
# now set up the database 
# ------------------------
python manage.py makemigrations
python manage.py migrate

# ------------------------
# now create super user and enter credentials
# ------------------------
python manage.py createsuperuser

# ------------------------
# check the system
# ------------------------
python manage.py check

# ------------------------
# run the website
# ------------------------
python manage.py runserver
```

# help URLs 
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html