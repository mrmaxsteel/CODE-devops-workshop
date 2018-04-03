FROM python:2

COPY flask-test-kata/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
