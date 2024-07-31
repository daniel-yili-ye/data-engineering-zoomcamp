FROM python:3.12

RUN apt-get update && apt-get install -y wget
RUN pip install --upgrade pip
RUN pip install pandas sqlalchemy psycopg2 pyarrow  # Added pyarrow

WORKDIR /app
COPY ingest-data.py ingest-data.py

ENTRYPOINT [ "python", "ingest-data.py" ]