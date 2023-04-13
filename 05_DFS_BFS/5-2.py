from collections import deque
#queue를 이용하여 선입선출을 구현함.
#popleft를 사용하면 선출, pop을 사용하면 후출 한다.
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

l = list(queue)
print(l)
l.append(2)
l.pop()
print(l)

queue.append(2)
queue.popleft()
print(queue)
