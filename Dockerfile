FROM python:2
# Install the required python packages 
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy flask app source code to the /app dir on the container
WORKDIR /app/
COPY app/ .
# Set the Entrypoint to start the calculator app
CMD ["python", "calculator/app.py"]

