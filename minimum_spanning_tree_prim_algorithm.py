"""
Purpose: 
    - get cost (minimum sum of edges) to visit all of the vertex
Steps:
    1. Pilih sembarang vertex sebagai titik awal
    2. Tambahkan adjacent vertex
        Pilih tetangga dengan bobot terkecil yang tidak membentuk siklus.
        This automatically handled by min-heap and visited set.
    3. Ulangi langkah 2 sampai semua vertex dikunjungi
    
>>> prim(adj)
Total weight: 16
"""

n = 6
adj = [[] for i in range(n)]

def addPath(source, dest, weight):
    adj[source].append((weight, dest))
    adj[dest].append((weight, source))

addPath(0, 1, 1)
addPath(0, 3, 4)
addPath(0, 4, 3)
addPath(1, 4, 2)
addPath(3, 4, 4)
addPath(1, 3, 4)
addPath(4, 2, 4)
addPath(4, 5, 7)
addPath(5, 2, 5)

import heapq

def prim(adj):
    pq = []
    heapq.heappush(pq, (0, 0))
    visited = set()
    cost = 0
    
    while pq:
        uWeight, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        cost += uWeight
        
        for vWeight, v in adj[u]:
            heapq.heappush(pq, (vWeight, v))
    
    print(f'Total weight: {cost}')

import doctest
doctest.testmod(verbose=True)
