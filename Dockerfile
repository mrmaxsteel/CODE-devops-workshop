FROM python:2 as builder
COPY flask-test-kata/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM python:2
COPY flask-test-kata/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/
COPY flask-test-kata/ .
CMD ["python", "calculator/app.py"]

