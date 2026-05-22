FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt pyproject.toml ./
COPY src ./src
COPY scripts ./scripts
COPY data/sample ./data/sample

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/src

CMD ["python", "scripts/run_training_pipeline.py", "--input", "data/sample/customers.csv", "--artifact-dir", "artifacts"]
