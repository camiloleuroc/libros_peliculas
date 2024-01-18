# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY microservicios.py /app/

RUN pip install flask

CMD ["python", "/app/microservicios.py"]
