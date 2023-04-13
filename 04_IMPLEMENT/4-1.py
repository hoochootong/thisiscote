# 여기서 X, Y를 좌표측의 x,y 축으로 생각하면 혼란스럽다.
# x를 행, y를 열로 생각하자. 행렬이다.
# 혼돈 된다면 row, col이 적절하고 그게 옳은 것 같다. 
n = int(input())
x, y = 1, 1
plans = input().split()
result_x = 0
result_y = 0

move_y = [-1, 1, 0, 0]
move_x = [0, 0, -1, 1]
symbols = {"L": 0, "R": 1, "U": 2, "D": 3}

for plan in plans:
  to_x = x + move_x[symbols[plan]]
  to_y = y + move_y[symbols[plan]]

  if (to_x < 1 or to_x > n or to_y < 1 or to_y > n):
    continue
  x = to_x
  y = to_y

print(str(x) + " " + str(y))
