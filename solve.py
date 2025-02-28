if solve(puzzle ,0,0):
  for i in range(9):
    for j in range(9):
      print(puzzle[i][j],end=" ")
    print()
else:
  print("No solution")
