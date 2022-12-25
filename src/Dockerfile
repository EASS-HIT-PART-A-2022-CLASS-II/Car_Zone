FROM python:3.10.0

WORKDIR /app/src
WORKDIR /app

COPY . /app/src
COPY ./requierments.txt /app

RUN pip3 install -r requierments.txt

EXPOSE 8000

CMD ["uvicorn","src.main:app","--host=0.0.0.0","--reload"]
