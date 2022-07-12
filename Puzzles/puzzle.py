#Python chess library: https://python-chess.readthedocs.io/en/latest/

import chess
#sample data from https://database.lichess.org/


sample_puzzle_data = "00sHx,q3k1nr/1pp1nQpp/3p4/1P2p3/4P3/B1PP1b2/B5PP/5K2 b k - 0 17,e8d7 a2e6 d7d8 f7f8,1760,80,83,72,mate mateIn2 middlegame short,https://lichess.org/yyznGmXs/black#34,Italian_Game,Italian_Game_Classical_Variation"
sample_puzzle_data2 = "00sJ9,r3r1k1/p4ppp/2p2n2/1p6/3P1qb1/2NQR3/PPB2PP1/R1B3K1 w - - 5 18,e3g3 e8e1 g1h2 e1c1 a1c1 f4h6 h2g1 h6c1,2671,105,87,325,advantage attraction fork middlegame sacrifice veryLong,https://lichess.org/gyFeQsOE#35,French_Defense,French_Defense_Exchange_Variation"
split_data = sample_puzzle_data.split(',') # for demonstration only, may choose to use a library to handle a csv file

board = chess.Board(split_data[1])
moves = split_data[2].split()

ai_moves = moves[::2]
player_moves = moves[1::2]

player_move_count = 0

print(board)

for move in ai_moves:
    print("Opponent Moving...")
    board.push(chess.Move.from_uci(move))
    print(board)
    player_input = input("Enter the move you'd like to perform in the following format: [starting tile][ending tile] Ex: a2a4  ")
    while not player_input == player_moves[player_move_count]:
        player_input = input("That's not quite the optimal move. Try Again:  ")
    print("Correct!")
    board.push(chess.Move.from_uci(player_moves[player_move_count]))
    print(board)
    player_move_count += 1
