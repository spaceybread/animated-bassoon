class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        blah = defaultdict(list)
        vals = set()

        for i in range(len(nums)):
            vals.add(nums[i])
            blah[nums[i]] += [i]

        best = 10**7 + 1
        for x in list(vals):
            li = blah[x]

            if len(li) < 3: continue

            for i in range(len(li) - 2): best = min(best, 2 * (li[i + 2] - li[i]))        
        
        return best if best != 10**7 + 1 else -1 