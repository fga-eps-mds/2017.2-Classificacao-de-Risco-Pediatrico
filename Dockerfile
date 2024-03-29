FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libxft-dev \
    libpq-dev \
    python-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

#RUN useradd -m myuser
#USER myuser

#RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:$PORT