FROM python:3.8 AS python

WORKDIR /code

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code/app/output/

ENTRYPOINT ["python", "-m", "http.server"]