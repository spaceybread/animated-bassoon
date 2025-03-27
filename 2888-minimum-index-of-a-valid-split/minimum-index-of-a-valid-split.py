class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        f, d = Counter(nums), -1
        for k, v in f.items():
            if v > len(nums) / 2: 
                d = k
                break
        
        fd = 0
        for i in range(len(nums)):
            if nums[i] == d: fd += 1
            if (i + 1) // 2 < fd and (len(nums) - i - 1) // 2 < f[d] - fd: return i
        return -1