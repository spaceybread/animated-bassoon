class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        a = sorted(list(nums))
        heapq.heapify(a)
        out = 0

        while len(a) > 1:
            x = heapq.heappop(a)
            if x >= k: return out
            y = heapq.heappop(a)
            out += 1
            heapq.heappush(a, min(x, y) * 2 + max(x, y)) 
        return out