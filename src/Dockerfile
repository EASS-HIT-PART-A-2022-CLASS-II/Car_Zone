FROM python:3.10.0

WORKDIR /app/src
WORKDIR /app

COPY . /app/src
COPY ./requierments.txt /app

RUN pip3 install -r requierments.txt


CMD ["uvicorn", "src.main:app", "--host","0.0.0.0","8080"]
