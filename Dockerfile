FROM python:3.10-slim


ENV WORKDIR_ROUTE /app
ENV PORT 8000
ENV PYTHONUNBUFFERED True


WORKDIR ${WORKDIR_ROUTE}


COPY . ${WORKDIR_ROUTE}


RUN pip install -r requirements.txt


EXPOSE ${PORT}


CMD gunicorn --bind :${PORT} --workers 1 --threads 8 --timeout 0 src.app:app
