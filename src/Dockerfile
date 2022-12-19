FROM python:3.10.0

COPY ./src /app/src
COPY ./requierments.txt /app

WORKDIR /app/src
WORKDIR /app

RUN pip3 install -r requierments.txt


EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0","--reload"]
