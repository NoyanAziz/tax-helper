# Tax Helper Chat App

##  Live Hosting
https://tax-helper-frontend.vercel.app/

## Reading Materials used

### Custom user created using

https://testdriven.io/blog/django-custom-user-model/

### Next App created using official docs

https://nextjs.org/docs

### Django App created using offical docs

https://www.django-rest-framework.org/

https://docs.djangoproject.com/en/5.0/

### Deployment made using following docs

Frontend: https://vercel.com/docs
Backend: https://www.koyeb.com/docs/deploy/django
Celery[redis]: https://www.koyeb.com/tutorials/deploy-a-python-celery-worker

## Installation

### Repo Clone

1. `git clone https://github.com/NoyanAziz/tax-helper.git`
2. `git status`

You might be asked a username and password. For password you'll need to create an access token

### NextJs App
Go to the tax-helper-frontend/ and run the following commands.

1. `npm i`
2. `npm run build`
3. `npm run dev`
4. In the src/app/constants/routes.js change the BACKEND_BASE_ROUTE to `http://localhost:8000/`

In case you are facing issues with `npm i` upgrade your node version to 21. You can use nvm for having multiple node versions in your app for further info visit:
https://github.com/nvm-sh/nvm/blob/master/README.md

### Django App
Once your frontend server has started, make sure to setup django. For that you will need to make a few changes to the code

1. Go to the tax_helper/ directory in root
2. Create a local db and set it up in the tax_helper/settings.py, follow this link https://www.w3schools.com/postgresql/postgresql_pgadmin4.php
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.getenv('DB_NAME'),
         'USER': os.getenv('DB_USER'),
         'PASSWORD': os.getenv('DB_PASSWORD'),
         'HOST': os.getenv('DB_HOST'),
         'PORT': os.getenv('DB_PORT'),
     }
 }
```
2. Comment out
```
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}
```
3. Add a .env of the format and add your keys
```
SECRET_KEY='your-secret-key'
DEBUG=True
DB_NAME='your-db-name'
DB_USER='your-db-user'
DB_PASSWORD='your-db-pass'
DB_HOST='localhost'
DB_PORT='5432'
GROQ_API_KEY='your-groq-api'
DB_URL=''
```
4. run `pip install -r requirements.txt` to install packages
5. run `python manage.py migrate` to migrate database
6. run `python manage.py createsuperuser` to create your super user
7. run `python manage.py runserver` to start the server

### Run celery

1. Install redis to your machine using https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/
2. In the tax_helper/settings.py update **CELERY_BROKER_URL** and **CELERY_RESULT_BACKEND** to `redis://localhost:6379/0`
3. Run `celery -A tax_helper worker -l info`

### Groq cloud API Key
Go to https://console.groq.com/keys and get your api key and add it into your .env file

### Sample W2 data files

1. [Copy of TaxGPT W-2 - 2 by 2 Black.pdf](https://github.com/NoyanAziz/tax-helper/files/15176580/Copy.of.TaxGPT.W-2.-.2.by.2.Black.pdf)
2. [Copy of TaxGPT W-2 - 1 by 3.pdf](https://github.com/NoyanAziz/tax-helper/files/15176579/Copy.of.TaxGPT.W-2.-.1.by.3.pdf)




---- Now the setup is completed for you to run on your local machine ----
