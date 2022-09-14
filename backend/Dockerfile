FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system

EXPOSE 8000

# CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
