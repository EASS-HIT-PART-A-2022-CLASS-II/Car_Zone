FROM python:3.11.1

COPY ./src /app/src
COPY ./requierments.txt /app

WORKDIR /app

RUN pip3 install -r requierments.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0","--reload"]
