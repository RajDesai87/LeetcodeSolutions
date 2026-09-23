class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minheap = [(x * x + y * y, [x, y]) for x, y in points]
        heapq.heapify(minheap)
        return [heapq.heappop(minheap)[1] for _ in range(k)]