FROM python:2 AS builder
# Install the required python packages 
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy flask app source code to the /app dir on the container
WORKDIR /app/
COPY app/ .

FROM builder AS unit-tester
RUN py.test ./tests/unit -v \
  --junitprefix=linux \
  --junitxml unit_results.xml || true

FROM unit-tester AS integration-tester
RUN py.test ./tests/integration -v \
  --junitprefix=linux \
  --junitxml integration_results.xml || true

FROM python:2-alpine AS production
WORKDIR /app/
COPY --from=builder /app .
# Start the calculator app when you run this container
CMD ["python", "calculator/app.py"]
