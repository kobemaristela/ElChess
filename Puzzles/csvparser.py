import pandas as pd
import multiprocessing as mp
from fenparser import FenParser
from pyarrow import csv as arrow

class CsvParse():
    def __init__(self, csv_file, workers=4, chunksize=101):
        self.csv = csv_file
        self.workers = workers
        self.chunksize = chunksize
    
    def pyarrow_parse(self):
        read_options = arrow.ReadOptions(autogenerate_column_names=True)
        read = arrow.read_csv(self.csv, read_options=read_options)
        print(read)

    def parse(self):
        read = pd.read_csv(self.csv, engine="pyarrow")
        worker = mp.Pool(self.workers)

        procs = []

        for line in read:
            f = worker.apply_async(self.proc,[line])
            procs.append(f)

    def proc(self, fen):
        print(fen)
        data = FenParser(fen)

if __name__ == "__main__":
    file_path = r"C:\Users\Kobe\Desktop\projects\project-1\Puzzles\lichess_db_puzzle.csv"
    p = CsvParse(file_path)
    p.pyarrow_parse()