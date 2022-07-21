import pathlib
import time
import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.csv as pv



CSV_NAME = r'lichess_db_puzzle'
PARQUET_NAME = r'lichess_db_puzzle2'


class ParquetConverter():
    def __init__(self, csv_name, parquet_name, chunksize=100_000):
        cwd = pathlib.Path(__file__).parent.resolve()
        self.csv = cwd.joinpath(csv_name + ".csv")
        self.parquet = cwd.joinpath(parquet + ".parquet")
        self.chunksize = chunksize
        

    def csv_to_parquet_pandas(self, **csv_kwargs):
        if os.path.exists(self.parquet):
            return False

        print(f"Converting CSV {self.csv} to PARQUET {self.parquet} using Pandas")
        csv_stream = pd.read_csv(
            self.csv, sep="\t", chunksize=self.chunksize, low_memory=False, **csv_kwargs)

        parquet_schema = None
        parquet_writer = None
        for i, chunk in enumerate(csv_stream):
            print("Chunk", i)
            if not parquet_schema:
                # Guess the schema of the CSV file from the first chunk
                parquet_schema = pa.Table.from_pandas(df=chunk).schema
                # Open a Parquet file for writing
                parquet_writer = pq.ParquetWriter(
                    self.parquet, parquet_schema, compression="snappy")
            # Write CSV chunk to the parquet file
            table = pa.Table.from_pandas(chunk, schema=parquet_schema)
            parquet_writer.write_table(table)

        parquet_writer.close()


    def csv_to_parquet_pyarrow(self):
        if os.path.exists(self.parquet):
            return False

        print(f"Converting CSV {self.csv} to PARQUET {self.parquet} using PyArrow")

        parse_options = pv.ParseOptions(delimiter="\t")
        csv_stream = pv.read_csv(csv, parse_options=parse_options)
        pq.write_table(csv_stream, self.parquet)
