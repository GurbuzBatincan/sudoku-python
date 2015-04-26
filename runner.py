from sudoku import *

f = open('set-01_sudoku_puzzles.txt', 'r')

for i, line in enumerate(f):
  game = Sudoku(line.strip())
  game.solve()
  print(i + 1)
  print(game) #if game.solved() else None
  print(game.to_pos())