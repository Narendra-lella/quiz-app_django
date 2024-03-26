FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /main

COPY requirements.txt /main/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /main/

EXPOSE 8000

RUN python manage.py makemigrations

RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]