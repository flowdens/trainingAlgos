def findShortestPaths(n: int, flights: List[List[int]]) -> List[List[int]]:
    A = [0] * n

    for i in range(0, n):
        A[i] = [0] * n
        for j in range(0, n):
            if i != j:
                A[i][j] = math.inf

    for flight in flights:
        s, t, c = flight
        A[s][t] = c

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
    return A
