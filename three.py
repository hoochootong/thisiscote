n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(n, m, k, data)
first = data[0]
second = data[1]
result = 0

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = first * count
result += second * (m - count)

print("three", result, m)