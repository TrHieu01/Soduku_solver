def is_valid_move(grid,row, col, number):
  for x in range(9):
    if grid[row][x] == number:
      return False
  for x in range(9):
    if grid[x][col] == number:
      return False
  
  conner_row = (row // 3) * 3
  conner_col = (col // 3) * 3
  for r in range(3):
    for c in range(3):
      if grid[conner_row + r][conner_col + c] == number:
        return False
  return True




def solve(grid, row, col):
  if col == 9:
    if row == 8:
      return True
    row += 1
    col = 0
  if grid[row][col] > 0:
    return solve(grid, row, col + 1)

  for num in range(1,10):
    if is_valid_move(grid, row, col, num):
      grid[row][col] = num
      if solve(grid, row, col + 1):
        return True
    grid[row][col] = 0
  return False


