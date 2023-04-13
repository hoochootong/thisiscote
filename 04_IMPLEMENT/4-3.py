input = input()
row = int(input[1])
col = ord(input[0]) - ord('a') + 1



print(col, row)

moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
result = list()

for move in moves:
  to_row = row + move[0]
  to_col = row + move[1]

  if to_row < 1 or to_row > 8 or to_col < 1 or to_col > 8:
    continue
  
  result.append(move)

print(result)

  
  