# input_data = input()

# row = int(input_data[1])
# col =int(ord(input_data[0])) - int(ord('a')) + 1
# steps = [[-1, -2], [1, -2], [-1, 2], [1, 2],
#         [-2, -1], [-2, 1], [2, -1], [2, 1]]

# result = 0
# for step in steps:
#   next_row = row + step[0]
#   next_col = col + step[1]

#   if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <=8:
#     result += 1

# print(str(result))

# for i in range(4 + 1):
#   print(i)

def factorial_recursive(n):
  if n <= 1:
    return n
  return n * factorial_recursive(n - 1)
def factorial_iterative(n):
  res = 1
  for i in range(1, n + 1):
    print(i)
    res = res * i
  return res
    
print(factorial_iterative(5))