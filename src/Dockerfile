# can't use Alpine version as it does hav the C stuff to build pandas and numpy
FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get update
RUN apt-get install -y python3-pip
# RUN apk add --no-cache --update \
# 	python3 python3-dev gcc \
# 	gfortran musl-dev g++ \
# 	libffi-dev openssl-dev \
# 	libxml2 libxml2-dev \
# 	libxslt libxslt-dev \
# 	libjpeg-turbo-dev zlib-dev

RUN pip3 install --upgrade pip

# install Pandas/Numpy here
# RUN pip3 install Flask==1.0.2 \
# 	pytest==4.6.2 \
# 	numpy==1.15.4 \
# 	pandas==0.23.4

WORKDIR /app

# Backup the default app files.  You could also delete these
RUN mkdir bak && \
	mv main.py uwsgi.ini bak

# Copy the Flask application's file in /app
COPY ./ ./

# install our dependencies
RUN pip3 install -r requirements.txt

# Make /app/* available to be imported by Python globally to better support several
ENV PYTHONPATH=/app