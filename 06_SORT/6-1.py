# Merge Sort
# 배열의 index를 활용하는 것을 기억하자. 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min = i
  for j in range(i + 1, len(array)):
    if array[j] < array[min]:
      min = j
  array[i], array[min] = array[min], array[i]

print(array)
