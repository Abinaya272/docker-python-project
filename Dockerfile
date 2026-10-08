FROM python:3.12

WORKDIR /app

RUN pip install flask

COPY app.py .

EXPOSE 80

CMD ["python", "app.py"]