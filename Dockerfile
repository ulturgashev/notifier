FROM python:3.7-alpine

RUN apk update && apk upgrade
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

ENV LC_ALL=C
COPY . .
CMD ["python", "app.py"]
