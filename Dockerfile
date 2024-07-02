FROM python:3.10-slim


ENV PORT 8000
ENV PYTHONUNBUFFERED True


WORKDIR /app


COPY . /app/


RUN pip install -r requirements.txt


EXPOSE ${PORT}


CMD hypercorn src.app:app --bind :${PORT} --workers 1 --threads 8 --log-level debug --reload
