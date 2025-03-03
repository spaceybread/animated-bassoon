class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        le, et, gt = [], [], []
        for a in nums:
            if a < pivot: le.append(a)
            if a == pivot: et.append(a)
            if a > pivot: gt.append(a)
        
        return le + et + gt