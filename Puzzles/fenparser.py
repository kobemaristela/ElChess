from itertools import chain
import re

class FenParser():
  def __init__(self, fen):
    self.fen = fen

  def parse(self):
    ranks = self.fen.split(" ")[0].split("/")
    rankPieces = [self.parse_rank(rank) for rank in ranks]
    return rankPieces

  def parse_rank(self, rank):
    regExp = re.compile("(\d|[kqbnrpKQBNRP])")
    matches = regExp.findall(rank)
    pieces = self.flatten(map(self.expand, matches))
    return pieces

  def flatten(self, lst):
    return list(chain(*lst))

  def expand(self, pieceString):
    regExp = re.compile("([kqbnrpKQBNRP])")
    res = ""
    if regExp.match(pieceString):
      res = pieceString
    else:
      res = self.padding(pieceString)
    return res

  def padding(self, num_str):
    return int(num_str)*" "


if __name__ == "__main__":
  fen = "r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1"
  p = FenParser(fen)

  [print(rank) for rank in p.parse()]