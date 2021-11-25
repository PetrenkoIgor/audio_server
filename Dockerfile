FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN apt-get update -y
RUN apt-get install libgirepository1.0-dev -y
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]