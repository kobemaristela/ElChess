import multiprocessing as mp
from pathlib import Path

import pyarrow.parquet as arrowParquet

from fenparser import FenParser
from parquetconverter import ParquetConverter


class PuzzleDatabase():
    def __init__(self, database, search=None, workers=mp.cpu_count()):
        self.database = database
        self.workers = workers
        self.search = search
        self.results = []

    """
    Statistics on Pyarrow with Parquet
    https://github.com/tirthajyoti/Machine-Learning-with-Python/blob/master/Pandas%20and%20Numpy/Read_data_various_sources/Pandas%20CSV%20vs.%20PyArrow%20parquet%20reading%20speed.ipynb
    """
    def __pyarrow_parse_parquet(self):
        table = arrowParquet.read_table(self.database)
        pool = mp.Pool(self.workers)

        for chunk in table:
            for line in chunk:
                pool.apply_async(self._process_string, [line.as_py()])

        pool.close()
        pool.join()

    def _process_string(self, fen):
        fen_str = fen.split(',')[1]
        fen_parser = FenParser(fen_str)
        if fen_parser.search_piece(self.search):
            self.results.append(fen)

    def main(self):
        """
        @TODO: create check for csv file
        """
        if not self.database.with_suffix('.parquet').is_file():
            if Path(self.database).suffix != '.parquet':
                convert = ParquetConverter(self.database,
                                            self.database.with_suffix('.parquet'))
                if convert.csv_to_parquet_pyarrow():
                    self.database = self.database.with_suffix('.parquet')

        self.__pyarrow_parse_parquet()

    def read_results(self):
        return self.results

if __name__ == "__main__":
    cwd = Path(__file__).parent.resolve()
    db = PuzzleDatabase(cwd.joinpath('lichess_db_puzzle.csv'),'Pp')
    db.main()

    db.read_results()