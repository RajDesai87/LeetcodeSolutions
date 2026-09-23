class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n=len(matrix)
        l=[(matrix[r][0],r,0) for r in range(n)]
        heapq.heapify(l)
        ans=0
        for i in range(k):
            temp=heapq.heappop(l)
            ans,r,c=temp[0],temp[1],temp[2]
            if c+1 < n:
                heapq.heappush(l,(matrix[r][c+1],r,c+1))
        return ans