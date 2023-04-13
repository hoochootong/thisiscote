n, m, k = map(int, input().split())

data = [2, 4, 5, 4, 6]

print("nmk", n, m, k)

# 큰수를 구하기 위한 데이터 정렬
data.sort(reverse=True) 
print(data)
first = data[0]
second = data[1]
print(first, second)
result = 0

# 큰수는 k 만큼 반복 후 2번째 수를 더하며, m만큼 반복하는 것이 핵심
# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result = result + first
#     m = m - 1
#   if m == 0:
#     break
#   result = result + second
#   m = m - 1

# print(result)

# 위 반복문의 시간복잡도는 o(n * n) 
# 아래는 수열 원리에 입각



count = (int)(m / (k+1)) * k #큰수가 반복되는 횟수
count = count + (m % (k+1)) #나머지가 0이 아닌 경우 더 반복되는 횟수
sum = count * first # 가장 큰 수의 합 계산
sum = sum + (second * ( m - count))# 두번째로 큰 수 더하기
print("here")
print(sum)
