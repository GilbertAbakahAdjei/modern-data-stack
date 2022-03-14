FROM python:3.9
ADD . /code
WORKDIR /code
COPY . .
RUN apt-get update
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
# RUN pip-compile requirements.in
