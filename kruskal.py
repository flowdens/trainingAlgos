# https://leetcode.com/problems/min-cost-to-connect-all-points/

from functools import reduce
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weights = {}
        # make weights matrix
        self.initiate(weights, points)
        
        n = len(points)
        size = [1 for x in range(0, n)] # size of growing subtree
        name = [x for x in range(0, n)] # name[v] is name of the tree of vertix v
        nxt = [x for x in range(0, n)] # inside this list we store (as linked list) vertices of subtree to rename them in merge()

        tree = set()
        sortedEdges = sorted(weights.keys(), key=lambda x: weights[x])
        m = len(sortedEdges)

        for i in range(0, m):
            # let's tale the minimum weught edge
            edge = sortedEdges[i]
            v, w = edge[0], edge[1]

            # if they belong to different subtrees, take this edge to the minimum spanning tree
            if name[v] != name[w]:
                tree.add(edge)
                if size[w] <= size[v]: # lets rename smallest tree (to optimize)
                    self.merge(v, w, size, name, nxt)
                else:
                    self.merge(v, w, size, name, nxt)

            if len(tree) == n - 1: # it's a feature of tree that m (amout of edges) = n (amount of vertices)- 1
                break

        s = 0
        for i in tree: #(order is not important)
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

        # to make it cycled (just so by design)
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
        
