from python:3
env PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .