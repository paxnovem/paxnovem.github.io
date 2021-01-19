FROM python:3.8 AS python

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /code/app/output/

ENTRYPOINT ["python", "-m", "http.server"]