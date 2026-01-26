FROM python:3.10-slim AS tester
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

RUN PYTHONPATH=. python3 -m pytest

FROM python:3.10-slim
WORKDIR /app

COPY --from=tester /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=tester /app/app ./app

RUN mkdir -p logs

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]