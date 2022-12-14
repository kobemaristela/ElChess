import csv
import multiprocessing as mp
import pyarrow.parquet as arrowParquet

from pathlib import Path
from .fenparser import FenParser
from .parquetconverter import ParquetConverter
from ..constants import *


"""
Statistics on Pyarrow with Parquet
https://github.com/tirthajyoti/Machine-Learning-with-Python/blob/master/Pandas%20and%20Numpy/Read_data_various_sources/Pandas%20CSV%20vs.%20PyArrow%20parquet%20reading%20speed.ipynb
"""
class PuzzleDatabase():
    def __init__(self, search=None, database=NORMAL_DATABASE, workers=mp.cpu_count()):
        self.database = database
        self.workers = workers
        self.search = search
        self.results = []
        self.easy = []
        self.normal = []
        self.hard = []
        self.puzzles = {'KkpP': 0, 'KkPpNn': 0, 'KkPpNnBb': 0, 'KkPpNnBbRr': 0, 'KkPpNnBbRrQq': 0}



    """
    WRITE DATABASE FOR PUZZLE

    """
    def __pyarrow_write_parquet(self):
        table = arrowParquet.read_table(self.database)
        pool = mp.Pool(self.workers)

        for chunk in table:
            if len(self.easy) > 1000 and len(self.normal) > 1000 and len(self.hard) > 1000:
                break
            for line in chunk:
                print(len(self.easy), len(self.normal), len(self.hard))
                if len(self.easy) > 1000 and len(self.normal) > 1000 and len(self.hard) > 1000:
                    break
                pool.apply_async(self._process_write_puzzle, [line.as_py()], callback=self._record_write_results)

        pool.close()
        pool.join()


    def _process_write_puzzle(self, puzzles):
        if puzzles:
            puzzle = puzzles.split(',')
            rating = int(puzzle[3])

            
            fen_parser = FenParser(puzzle[1])
            for search in ['KkPp', 'KkPpNn', 'KkPpNnBb', 'KkPpNnBbRr', 'KkPpNnBbRrQq']:
                print(f"Current Readings: {self.puzzles}")
                if fen_parser.search_piece(search):
                    print(f"My count: {self.puzzles[search]} for {search}")

                    if rating < 2000:
                        return puzzle[1:4]
        return None
        

    def _record_write_results(self, puzzle):
        if puzzle:
            rating = int(puzzle[2])
            print(f"Current Readings: {self.puzzles}")
            self.puzzles[search] += 1
            if rating <= 800 and len(self.easy) <= 1000: 
                # print(rating, puzzle)
                self.easy.append(puzzle)
            
            if rating > 800 and rating < 1400 and len(self.normal) <= 1000:
                # print(rating, puzzle)
                self.normal.append(puzzle)
            
            if rating >= 1400 and rating < 2000 and len(self.hard) <= 1000:
                # print(rating, puzzle)
                self.hard.append(puzzle)
        return None


    def write_results(self):
        print("Preparing to write puzzles...")
        
        if self.easy:
            print("Writing Easy Puzzles...")
            with open(EASY_DATABASE, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(self.easy)

        if self.normal:
            print("Writing Normal Puzzles...")
            with open(NORMAL_DATABASE, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(self.normal)
        
        if self.hard:
            print("Writing Hard Puzzles...")
            with open(HARD_DATABASE, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(self.hard)



    """
    READ DATABASE FOR PUZZLE

    """
    def __pyarrow_read_parquet(self):
        table = arrowParquet.read_table(self.database)
        pool = mp.Pool(self.workers)

        for chunk in table:
            for line in chunk:
                pool.apply_async(self._process_search_string, [line.as_py()], callback=self._record_read_results)

        pool.close()
        pool.join()


    def _process_search_string(self, fen):
        fen_str = fen.split(',')[0]
        fen_parser = FenParser(fen_str)

        if not self.search:
            return fen

        if fen_parser.search_piece(self.search):
            return fen


    def _record_read_results(self, puzzle):
        if puzzle:
            self.results.append(puzzle)


    def read_results(self, clear_results=False):
        if clear_results:
            temp = self.results
            self.results.clear()
            return temp
            
        return self.results




    def main(self, read=False, write=False):
        """
        @TODO: create check for csv file
        """
        print("Reading Database...")
        print(self.database)
        if not self.database.with_suffix('.parquet').is_file():
            if Path(self.database).suffix != '.parquet':
                convert = ParquetConverter(self.database,
                                            self.database.with_suffix('.parquet'))

                convert.csv_to_parquet_pyarrow()
                print(f"Conversion complete...")

        self.database = self.database.with_suffix('.parquet')
        
        print(f"Parsing Parquet file...")

        if read:
            self.__pyarrow_read_parquet()

        if write:
            self.__pyarrow_write_parquet()


if __name__ == "__main__":
    db = PuzzleDatabase(database=EASY_DATABASE)
    db.main(read=True)