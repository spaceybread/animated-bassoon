class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        a = sorted(list(nums))
        heapq.heapify(a)
        out = 0

        while a[0] < k:
            x = heapq.heappop(a)
            y = heapq.heappop(a)
            out += 1
            heapq.heappush(a, min(x, y) * 2 + max(x, y)) 
        return out