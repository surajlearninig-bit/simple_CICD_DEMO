FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY tests/ tests/

# Install your package in editable mode
RUN pip install -e src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

