from sudoku import *

# f = open('set-01_sudoku_puzzles.txt', 'r')
f = open('set-02_project_euler_50-easy-puzzles.txt', 'r')
# f = open('set-03_peter-norvig_95-hard-puzzles.txt', 'r')
# f = open('set-04_peter-norvig_11-hardest-puzzles.txt', 'r')

for i, line in enumerate(f):
  game = Sudoku(line.strip())
  game.solve()
  print(i + 1)
  print(game) #if game.solved() else None
<<<<<<< HEAD
  print(game.to_pos())
=======
  print(game.to_pos())
>>>>>>> e5196f773e073ae3c790b5b300307146bd7144c0
