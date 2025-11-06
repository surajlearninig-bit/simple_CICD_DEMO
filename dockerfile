FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY tests/ tests/

# Set PYTHONPATH so Python can find your src modules
ENV PYTHONPATH=/app/src

# Default command to run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
