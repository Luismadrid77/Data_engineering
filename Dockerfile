FROM python:3.10

RUN pip3 install fastapi uvicorn pandas

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]