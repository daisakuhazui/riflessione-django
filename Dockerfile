FROM python:3.8.0
ENV PYTHONUNBUFFERED=1 LANG=ja_JP.UTF-8
RUN apt-get update -y && apt-get install -y postgresql-client \
                                            redis-server \
                                            locales && \
    echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=ja_JP.UTF-8

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
