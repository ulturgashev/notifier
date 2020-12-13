FROM python:3.7-alpine

RUN apk update && apk upgrade
# only for tests, need to be removed in the future
RUN apk add --no-cache --update python3-dev  gcc build-base
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

ENV LC_ALL=C
ENV PYTHONPATH=/usr/src/app
COPY . .
CMD ["python", "service/app.py"]
