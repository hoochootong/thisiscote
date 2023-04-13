def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result = result * i
  return result


def factorial_recursive(n):
  #종료조건이 중요
  if n == 1:
    return 1
  return n * factorial_recursive(n - 1)


n = int(input())
print(factorial_iterative(n))
print(factorial_recursive(n))
