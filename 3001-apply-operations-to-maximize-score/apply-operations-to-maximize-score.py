# not my solution, src: https://leetcode.com/problems/apply-operations-to-maximize-score/solutions/6593668/sieve-of-eratosthenes-monotonic-stack-simple-solution-runtime-100
# don't have time today but I don't want to miss my streak

MOD = 1000000007
n = 100001
cpf = [0] * n
for k in range(2, n):
    if cpf[k] == 0:
        for i in range(k, n, k):
            cpf[i] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        sc = [cpf[num] for num in nums] + [inf]
        st = [-1]
        cba = [0] * len(nums)
        for i, score in enumerate(sc):
            while sc[st[-1]] < score:
                j = st.pop()
                cba[j] = (i - j) * (j - st[-1])
            st.append(i)

        ans = 1
        for num, cnt in sorted(zip(nums, cba), key = lambda n: -n[0]):
            if k > cnt:
                ans = ans * pow(num, cnt, MOD) % MOD
                k -= cnt
            else: return ans * pow(num, k, MOD) % MOD 
        return -1