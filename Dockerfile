FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

# RUN apt-get update
RUN pip3 install --upgrade pip

# install Pandas/Numpy here
# RUN pip3 install Flask==1.0.2 \
# 	pytest==4.6.2 \
# 	numpy==1.15.4 \
# 	pandas==0.23.4

WORKDIR /app

# Copy the Flask application's file in /app
COPY ./ ./

# install our dependencies
RUN pip3 install -r requirements.txt