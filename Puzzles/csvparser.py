import multiprocessing as mp
from fenparser import FenParser
import pyarrow.parquet as arrowParquet


class CsvParse():
    def __init__(self, csv_file, workers=mp.cpu_count(), chunksize=101):
        self.csv = csv_file
        self.workers = workers

    # https://github.com/tirthajyoti/Machine-Learning-with-Python/blob/master/Pandas%20and%20Numpy/Read_data_various_sources/Pandas%20CSV%20vs.%20PyArrow%20parquet%20reading%20speed.ipynb
    def pyarrow_parse_parquet(self):
        read = arrowParquet.read_table(r'/home/kobem/Desktop/project-1/Puzzles/lichess_db_puzzle1.parquet')
        # columns=['PuzzleId','FEN','Moves','Rating','RatingDeviation','Popularity','NbPlays','Themes','GameUrl','OpeningFamily','OpeningVariation']
        pool = mp.Pool(self.workers)

        for line in read:
            for l in line:
                f = pool.apply_async(self.process_string,[l.as_py()])
                
        pool.close()
        pool.join()


    def process_string(self, fen):
        print(self.workers)
        temp = fen.split(',')
        print(temp)
        # data = FenParser(fen)

if __name__ == "__main__":
    file_path = r"/home/kobem/Desktop/project-1/Puzzles/lichess_db_puzzle.csv"
    p = CsvParse(file_path)
    p.pyarrow_parse_parquet()
