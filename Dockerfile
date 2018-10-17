FROM python:2 AS builder
# Install the required python packages 
WORKDIR /app/
# Copy flask app source code to the /app dir on the container
COPY app/ .
# Install the required python packages 
RUN pip install \
  --no-cache-dir \
  -r dev-requirements.txt
# Copy flask app source code to the /app dir on the container

FROM builder AS unit-tester
RUN py.test ./tests/unit -v \
  --junitprefix=linux \
  --junitxml unit_results.xml || true

FROM unit-tester AS integration-tester
RUN py.test ./tests/integration -v \
  --junitprefix=linux \
  --junitxml integration_results.xml || true
  
# Production image starts from the slimmer alpine container
FROM python:2-alpine AS production 
WORKDIR /app/
# Copy flask app source code to the /app dir on the container
COPY app/ .
# Install only the production requirements, not dev packages
RUN pip install \
  --no-cache-dir \
  -r requirements.txt
# Start the calculator app when you run this container
CMD ["python", "calculator/app.py"]
