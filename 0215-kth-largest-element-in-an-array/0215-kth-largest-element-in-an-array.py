import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l=[]
        heapq.heapify(l)
        for i in range(k):
            heapq.heappush(l,nums[i])
        for i in range(k,len(nums)):
            heapq.heappushpop(l,nums[i])
        return heapq.heappop(l)