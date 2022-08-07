from pathlib import Path
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.csv as pv


CSV_NAME = r'lichess_db_puzzle'
PARQUET_NAME = r'lichess_db_puzzle2'


class ParquetConverter():
    def __init__(self, csv, parquet, chunksize=100_000):
        self.csv = csv
        self.parquet = parquet
        self.chunksize = chunksize


    def csv_to_parquet_pandas(self):
        if Path(self.parquet).exists():
            return False

        print(f"Converting CSV {self.csv} to PARQUET {self.parquet} using Pandas")
        csv_stream = pd.read_csv(
            self.csv, sep="\t", chunksize=self.chunksize, low_memory=False)

        schema = None
        writer = None
        for chunk in csv_stream:
            if not schema:
                # Save schema of CSV file
                schema = pa.Table.from_pandas(df=chunk).schema
                # Create parquet writer
                writer = pq.ParquetWriter(
                    self.parquet, schema, compression="snappy")
            # Write CSV chunk to the parquet file
            table = pa.Table.from_pandas(chunk, schema=schema)
            writer.write_table(table)

        writer.close()

        return True


    def csv_to_parquet_pyarrow(self) -> bool:
        if Path(self.parquet).exists():
            return False

        print(f"Converting CSV {self.csv} to PARQUET {self.parquet} using PyArrow")

        parse_options = pv.ParseOptions(delimiter="\t")
        csv_stream = pv.read_csv(self.csv, parse_options=parse_options)
        pq.write_table(csv_stream, self.parquet)

        return True
