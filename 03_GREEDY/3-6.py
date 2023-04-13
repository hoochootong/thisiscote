n, k = map(int, input().split())
result = 0

count = 0

while True:
  multiplied = (n // k) * k
  result += (n - multiplied)
  n = multiplied
  if n < k:
    break
  result += 1
  n = (int)(n / k)
print(n)
result += (n - 1)  # 이게 진짜 애매하네??
print(result)
