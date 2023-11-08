import heapq

collection = [10, 3, 3, 4, 5, 6]
print(collection)
print()

heapq.heapify(collection)
result = heapq.heappop(collection)
print(result)
print(collection)
print()

heapq.heappush(collection, 1)
heapq.heappush(collection, 1)
print(collection)
print()

result = heapq.heappop(collection)
print(result)
print(collection)
print()

result = heapq.heappop(collection)
print(result)
print(collection)
print()

result = heapq.heappop(collection)
print(result)
print(collection)
