class Solution:
    def f(self, k, word):
        a, i, c = 0, 0, 0
        v = Counter()

        for j in range(len(word)):
            if word[j] in "aeiou": v[word[j]] += 1
            else: c += 1

            while len(v) == 5 and c > k:
                if word[i] in "aeiou": 
                    v[word[i]] -= 1
                    if v[word[i]] == 0: del v[word[i]]

                else: c -= 1
                i += 1
            a += (j - i + 1)
        return a


    def countOfSubstrings(self, word: str, k: int) -> int: return self.f(k, word) - self.f(k - 1, word)