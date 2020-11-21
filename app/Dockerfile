FROM python:3.8 AS python

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "-m", "http.server"]