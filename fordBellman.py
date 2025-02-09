    # search of the shortest path in the wheighted graph (weights can be both positive and negative)
    def FordBellman(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        A = {} # martix of whights
        for i in range(0, n):
            A[i] = {}
            for j in range(0, n):
                A[i][j] = math.inf

        for flight in flights:
            s, t, c = flight
            A[s][t] = c

        D = {} # D[v] is shortest path from srs to v
        for v in range(0, n):  # here we build D1(v)
            D[v] = A[src][v] 

        for i in range(2, n): # we build D[i](v)
            for w in range(0, n):
                for v in range(0, n):
                    if D[w] + A[w][v] < D[v]: # compare new and old paths to v
                        D[v] = D[w] + A[w][v] # set the shortest path
        return -1 if D[dst] == math.inf else D[dst] # in case the is no path
