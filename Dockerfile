FROM python:3.10-alpine
WORKDIR /nedviga/
COPY requirements.txt /nedviga/
RUN pip install -r requirements.txt

COPY . /nedviga/
