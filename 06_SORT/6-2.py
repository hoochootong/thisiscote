# Insertion Sort
# 맨 왼쪽은 정렬되어다고 전제하에
# 그 이후 j인덱스 부터 iteration 
# j -1 씩 비교하여 작은 수가 나타날때마다 삽입함
# 자기보다 작은 데이터를 만나면 그 위치에서 멈춤

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  # 인덱스 i부터 1까지 감소하며 반복하는 문법
  for j in range(i, 0, -1):
    # 한 칸씩 왼쪽으로 이동
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
    else:
      break

print(array)