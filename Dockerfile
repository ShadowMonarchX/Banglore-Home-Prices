FROM python:3.10-slim

WORKDIR /app

# Copy requirement files
COPY server/requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all source code
COPY server/ ./server/
COPY server/artifacts/ ./artifacts/
COPY client/ ./client/

# Expose port
EXPOSE 5050

# Run app
CMD ["python3", "server/server.py"]
