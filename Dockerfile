FROM python:3.6.5-slim-stretch
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && \
    apt install -y \
    gcc \
    mariadb-client \
    mariadb-common \
    libmariadb-dev \
    default-libmysqlclient-dev \
    python3-pymysql \
    musl-dev \
    libjpeg-dev \
    wget \
    make

COPY base/prod-entrypoint.sh /startup/
RUN chmod +x /startup/prod-entrypoint.sh

WORKDIR /tmp
RUN wget http://zlib.net/zlib-1.2.11.tar.gz && \
	tar -xzvf zlib* && \
	cd zlib* && \
	./configure && make && make install && \
	cd ..
RUN wget http://www.ijg.org/files/jpegsrc.v9d.tar.gz && \
	tar -xzvf jpeg* && \
	cd jpeg* && \
	./configure && make && make install && \
	cd ..

RUN mkdir /code
WORKDIR /code
ADD base/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD . /code/

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
