class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        i, j, k = 0, 1, 2
        best = 10**7 + 1

        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[i] == nums[j] == nums[k]:
                        best = min(best, abs(i - j) + abs(j - k) + abs(k - i))
                    k += 1
                j += 1
            i += 1
        
        return best if best != 10**7 + 1 else -1