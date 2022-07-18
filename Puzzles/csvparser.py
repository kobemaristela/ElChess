import pandas as pd
import multiprocessing as mp
from fenparser import FenParser

class CsvParse():
    def __init__(self, csvFile, workers=4, chunksize=1000):
        self.csv = csvFile
        self.workers = workers
        self.chunksize = chunksize

    def parse(self):
        read = pd.read_table(self.csv, chunksize=self.chunksize)
        worker = mp.Pool(self.workers)

        procs = []

        for line in read:
            f = worker.apply_async(proc,[line])
            procs.append(f)

    def proc(self, fen):
        data = FenParser(fen)

if __name__ == "__main__":
    file_path = "TEST PATH"