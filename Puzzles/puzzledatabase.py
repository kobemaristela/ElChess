import multiprocessing as mp
from pathlib import Path

import pyarrow.parquet as arrowParquet

from fenparser import FenParser
from parquetconverter import ParquetConverter


class PuzzleDatabase():
    def __init__(self, database, workers=mp.cpu_count()):
        self.database = database
        self.workers = workers

    def main(self):
        if Path(self.database).suffix != '.parquet':
            convert = ParquetConverter(self.database,
                                       self.database.with_suffix('.parquet'))
            if convert.csv_to_parquet_pyarrow():
                self.database = self.database.with_suffix('.parquet')

        self.pyarrow_parse_parquet()

    """
    Statistics on Pyarrow with Parquet
    https://github.com/tirthajyoti/Machine-Learning-with-Python/blob/master/Pandas%20and%20Numpy/Read_data_various_sources/Pandas%20CSV%20vs.%20PyArrow%20parquet%20reading%20speed.ipynb
    """
    def pyarrow_parse_parquet(self):
        table = arrowParquet.read_table(self.database)
        pool = mp.Pool(self.workers)

        for chunk in table:
            for line in chunk:
                pool.apply_async(self.process_string, [line.as_py()])

        pool.close()
        pool.join()

    def process_string(self, fen):
        print(self.workers)
        temp = fen.split(',')
        print(temp)


if __name__ == "__main__":
    cwd = Path(__file__).parent.resolve()
    db = PuzzleDatabase(cwd.joinpath('lichess_db_puzzle.csv'))
    db.main()
