class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self.parent[pu] = pv
        return True


class Solution:
    def minCostConnectPoints(self, points) -> int:
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([manhattanDist(points[i], points[j]), i, j])

        edges.sort()  # Sort increasing order by dist
        uf = UnionFind(n)
        ans = 0
        for d, u, v in edges:
            if uf.union(u, v):
                ans += d
                n -= 1
            if n == 1:
                break  # a bit optimize when we found enough n-1 edges!
        return ans


s = Solution()
inputSet = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(s.minCostConnectPoints(inputSet))
