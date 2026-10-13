FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY main.py ./

RUN pip install --no-cache-dir .

ENTRYPOINT ["python", "main.py"]