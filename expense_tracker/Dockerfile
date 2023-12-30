FROM python:3
RUN pip3 install django
COPY . .
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
