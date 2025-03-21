class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ind = defaultdict(int)
        g = defaultdict(list)
        for r, ing in zip(recipes, ingredients): 
            ind[r] = len(ing)
            for i in ing: g[i].append(r)
        
        out = []
        q = deque(supplies)
        recipes = set(recipes)
        while q: 
            x = q.popleft()
            if x in recipes: out.append(x)
            for xx in g[x]: 
                ind[xx] -= 1
                if ind[xx] == 0: q.append(xx)
        return out 