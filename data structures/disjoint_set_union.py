"""
Description: stores partition set into disjoint subsets.
Purpose: determine whether two elements belong to the same set or not.
Operations:
    Make set:
        add new element into a new set (containing only the new element). Initialize node size/rank.
    Find:
        find the root of element. Variety: usual, path compression, path halving
    Union:
        merge the two sets that have same parent into one set. If union by rank, then the new parent rank is increased by one.
        
>>> dsu = DisjointSetUnion(4) # create 1,2,3,4
>>> dsu.union(1, 2)
>>> dsu.union(3, 4)
>>> dsu.union(1, 3)
>>> print(dsu.parent)
[0, 1, 1, 1, 3]
>>> print(dsu.find(1))
1
>>> print(dsu.find(2))
1
>>> print(dsu.find(3))
1
>>> print(dsu.find(4))
1
"""

class DisjointSetUnion:
    def __init__(self, n): 
        # make set
        self.parent = list(range(n+1)) # use one indexing
        self.rank = [0] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
        
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
            
dsu = DisjointSetUnion(4) # create 1,2,3,4
dsu.union(1, 2)
dsu.union(3, 4)
dsu.union(1, 3)
print(dsu.parent)
print(dsu.find(1))
print(dsu.find(2))
print(dsu.find(3))
print(dsu.find(4))

import doctest
doctest.testmod(verbose=True)