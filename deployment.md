## DEPLOYMENT


## TABLE OF CONTENTS

* [Deployment process](#deployment-process)
    * [Create external database on ElephantSQL](#create-external-database-on-elephantsql)
    * [Create app on Heroku](#create-app-on-heroku)
    * [Connect database to local development web server](#connect-database-to-local-development-web-server)
    * [AWS deployment](#aws-deployment)

## Deployment process

### Create external database on ElephantSQL
- Go to ElephantSQL dashboard and click **Create a new Instance**
- Give your plan a Name, Select the Tiny Turtle (Free) plan and leave the Tags field blank
- Select region and a database centre near you
- Click **Create Instance**
- Return to the ElephantSQL dashboard and click on the database instance name for this project.

### Create app on Heroku
- Go to Heroku and click **New** to create a new app.
- Give the app a name, select the region closest and then click **Create App** to confirm.
- Open the settings tab and add the config var **DATABASE_URL**, and for the value, copy in the **Database URL** from ElephantSQL

### Connect database to local development web server
- In the terminal, install **dj_database_url** and **psycopg2**, to connect to the external database.

    **pip3 install dj_database_url==0.5.0 psycopg2**

- Update requirements.txt file with the newly installed packages.

    **pip freeze > requirements.txt**

- In the settings.py file, import **dj_database_url** underneath the import for os

  **import os**

  **import dj_database_url**

- Scroll to the DATABASES section and update it so that the original connection to sqlite3 is commented out and connected to the new ElephantSQL database instead. Paste in the ElephantSQL database URL:

  **DATABASES = {**
     **'default': dj_database_url.parse(‘database-url-here')**

   **}**

- In the terminal, run the showmigrations command to confirm you are connected to the external database:
  **python3 manage.py showmigrations**

- Migrate database models to the new database:

  **python3 manage.py migrate**

- Load in the fixtures- it is important to load categories first before loading products:

  **python3 manage.py loaddata categories**

  **python3 manage.py loaddata products**

- Create a superuser for the new database:

  **python3 manage.py createsuperuser**

- Create a superuser username and password - the email address can be left blank.

- To prevent exposing the database when pushing to GitHub, delete it again from settings.py and set it up again using an environment variable, then reconnect to the local sqlite database. Therefore, when the app is running on Heroku where the database URL environment variable will be defined, it will connect to Postgres and otherwise, it connects to sequel light.

- Install Gunicorn, which will act as a webserver, and freeze into the requirements file.

- Create a Procfile to tell Heroku to create a web dyno which will run Gunicorn to serve the Django app, then temporarily disable collectstatic so that Heroku won't try to collect static files during deployment.

- Add the hostname of the Heroku app to allowed hosts in settings.py and add localhost so that Gitpod will continue to work.

- Test app deployment is successful by adding and committing changes, pushing to GitHub, and then **git push Heroku master** to deploy to Heroku and check build progress in Heroku.

- For automatic deployment when pushing to GitHub, go to the app in Heroku, and on the deploy tab set it to **Connect to GitHub**

- Search for the relevant repository, and click **Connect** which enables automatic deploys.

- Remove the secret key from settings.py and generate a new secret key for the Heroku app.

- Replace the secret key setting in settings.py with the call to get it from the environment and use an empty key as default.

- Set debug to be true only if there's a variable called development in the environment, commit changes and push to GitHub.

- In Heroku view the build progress which shows automatic deployments are working.

## AWS Deployment

- Set up hosting for static and media files with AWS (Amazon Web Services). Specifically, using S3 (“Simple Storage Service”) 

- Create an s3 bucket and add the user's groups and security policies for it.

- Connect Django by installing packages **boto3** and **django-storages** and freeze the packages into the requirements.txt file so they get installed on Heroku when deployed.

- Add storages to installed apps in settings.py

- To connect Django to s3 update settings.py - add an if statement to check if there's an environment variable called **USE_AWS** in the environment.

- If so, define the **AWS_STORAGE_BUCKET_NAME**, the **AWS_S3_REGION_NAME**, the **access key**, and **secret access key**, from the environment which must be kept secret.

- Go to Heroku and add the AWS keys to the config variables.

- Add a key **USE_AWS** and set to true. so that the settings file knows to use the AWS configuration when deployed to Heroku.

- Remove the **disable collectstatic** variable to ensure Django will collect static files automatically and upload them to s3 during deployment to Heroku.

- In settings.py file indicate where our static files will be coming from in production which will be the bucket name s3.amazonaws.com.

- Tell Django that in production to use s3 to store static files whenever collectstatic is run, and that any uploaded product images go there. Do this by creating a custom class called static storage which will inherit the one from Django storages, giving it all its functionality, and then tell it that we want to store static files in a location from the settings.py file.

- In settings.py set static file storage to use the storage class just created, and that the location it should save static files is a folder called static.

- Repeat for media files by using the default file storage, and media files location settings.

- Override and explicitly set the URLs for static and media files, using our custom domain and the new locations, so when the project is deployed, Heroku will run **python3 manage.py collectstatic** during the build process, which will search through all apps and project folders looking for static files, which will be collected into a static folder in the s3 bucket automatically.




