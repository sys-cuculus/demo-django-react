FROM python:3.12

WORKDIR /app

COPY ../../server/requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ../../server .

EXPOSE 8000