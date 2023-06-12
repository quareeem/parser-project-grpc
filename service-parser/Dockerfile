FROM python:3.10.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./app.py /app/app.py

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
