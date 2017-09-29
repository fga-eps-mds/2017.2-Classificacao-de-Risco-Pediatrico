FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN useradd -m myuser
USER myuser

RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:$PORT