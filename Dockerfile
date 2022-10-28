FROM python:3.9.6-alpine3.14

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/testing

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# informing Docker that the container listens on the
# specified network ports at runtime i.e 8000.
EXPOSE 8000
# running server
CMD ["python", "/usr/src/testing/testingproject/manage.py", "runserver"]


#toexecute
#docker build -t testingproject_postgress_nginx . --this is without combining 2 or more services/wanna use without docker-compose
#Build the new image and spin up the two containers:
#$ docker-compose up -d --build
#$ docker-compose exec web python manage.py migrate --noinput
#django.db.utils.OperationalError: FATAL:  database "hello_django_dev" does not exist
#docker-compose down -v
#Ensure the default Django tables were created:
#$ docker-compose exec db psql --username=myuser --dbname=mydb
#You can check that the volume was created as well by running:

#$ docker volume inspect django-on-docker_postgres_data
