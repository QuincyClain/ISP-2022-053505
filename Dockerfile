FROM python:3.10.2-alpine

WORKDIR /usr/src/app

COPY . .

CMD ["python", "./task_1.py"]
