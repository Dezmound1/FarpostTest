FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./viewer /app/

RUN chmod +x ./run_django.sh
CMD ./run_django.sh
