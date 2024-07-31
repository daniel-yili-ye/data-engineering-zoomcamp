#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # Get the name of the file from url
    file_name = url.rsplit("/", 1)[-1].strip()

    # Download file from the web using wget
    os.system(f"wget {url} -O {file_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Open the Parquet file
    parquet_file = pq.ParquetFile(file_name)

    # Iterate over batches
    first_chunk = True
    for batch in parquet_file.iter_batches(batch_size=100000):
        t_start = time()
        df = batch.to_pandas()
        if first_chunk:
            df.head(n=0).to_sql(
                name="yellow_taxi_data", con=engine, if_exists="replace"
            )
            first_chunk = False
        df.to_sql("yellow_taxi_data", con=engine, if_exists="append")
        t_end = time()
        print(f"inserted another chunk... took {t_end-t_start:.2f} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest parquet data to Postgres")

    parser.add_argument("--user", required=True, help="user name for postgres")
    parser.add_argument("--password", required=True, help="password for postgres")
    parser.add_argument("--host", required=True, help="host for postgres")
    parser.add_argument("--port", required=True, help="port for postgres")
    parser.add_argument("--db", required=True, help="database name for postgres")
    parser.add_argument(
        "--table_name",
        required=True,
        help="name of the table where we will write the results to",
    )
    parser.add_argument("--url", required=True, help="url of the parquet file")

    args = parser.parse_args()

    main(args)
