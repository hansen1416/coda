FROM python:3.9.5-slim-buster

WORKDIR /api

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /api/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /api

ENTRYPOINT ["/api/entrypoint.sh"]