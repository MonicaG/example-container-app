FROM python:3.11.5-alpine
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]