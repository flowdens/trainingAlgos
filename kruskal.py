# https://leetcode.com/problems/min-cost-to-connect-all-points/

from functools import reduce
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weights = {}
        self.initiate(weights, points)
        
        n = len(points)
        print(n)
        size = [1 for x in range(0, n)]
        name = [x for x in range(0, n)]
        nxt = [x for x in range(0, n)]
        tree = set()
        sortedEdges = sorted(weights.keys(), key=lambda x: weights[x])
        m = len(sortedEdges)

        for i in range(0, m):
            edge = sortedEdges[i]
            v, w = edge[0], edge[1]
            if name[v] != name[w]:
                tree.add(edge)
                if size[w] <= size[v]:
                    self.merge(v, w, size, name, nxt)
                else:
                    self.merge(v, w, size, name, nxt)

            if len(tree) == n - 1:
                break

        s = 0
        for i in tree:
            s += weights[i]
        return int(s)

    def merge(self, v, w, size, name, nxt):
        p = name[v]
        q = name[w]

        name[w] = p
        u = nxt[w]
        while name[u] != p:
            name[u] = p
            u = nxt[u]
        
        v1 = nxt[v]
        w1 = nxt[w]
        nxt[v] = w1
        nxt[w] = v1
        size[p] = size[p] + size[q]

    def initiate(self, weights, points):
        pointer = 0
        dots = {}

        for p in points:
            dots[pointer] = p 
            pointer += 1

        for v in dots.keys():
            for w in dots.keys():
                if v != w and (w, v) not in weights:
                    weights[(v, w)]= self.calculateWeight(dots[v], dots[w])

    def calculateWeight(self, v, w) -> int:
        return math.fabs(v[0] - w[0]) + math.fabs(v[1] - w[1])
        
