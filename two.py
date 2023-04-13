n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(n, m, k, data)
first = data[0]
second = data[1]
result = 0
while True:
  for n in range(k):
    if m == 0:
      break
    result += first
    m = m - 1
  if m == 0: 
    break
  result += second
  m = m - 1

print(result, m)