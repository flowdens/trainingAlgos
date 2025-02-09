class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        D = [inf] * n
        visited = [False] * n
        A = {}

        for i in range(0, n):
            A[i] = {}
            for j in range(0, n):
                A[i][j] = math.inf

        for flight in flights:
            s, t, c = flight
            A[s][t] = c
            if s == src:
                D[t] = c

        for i in range(1, n):

            # find closest unvisited vertice
            minVertice = src
            for vertice in range(0, n):
                if visited[vertice] or D[vertice] >= D[minVertice]:
                    continue
                minVertice = vertice

            # mark it visited
            visited[minVertice] = True

            # update D with paths through this vertice
            for v in range(0, n):
                if D[minVertice] + A[minVertice][v] < D[v]:
                    D[v] = D[minVertice] + A[minVertice][v]

        return -1 if D[dst] == math.inf else D[dst]
