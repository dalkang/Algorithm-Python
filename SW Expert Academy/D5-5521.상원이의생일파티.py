from collections import deque
 
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    friends = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for m in range(M):
        a, b = map(int, input().split())
        friends[a][b] = b
        friends[b][a] = a

    q = deque()
    q.append((1,0))
    visited = [0] * (N+1)
    visited[1] = True
    join = 0

    while len(q):
        next, cnt = q.popleft()
        if cnt == 2:
            break
        for i in range(1, N+1):
            if friends[next][i] and not visited[i]:
                q.append(((i,cnt+1)))
                visited[i] = True
                join += 1
                
    print("#%d %d" % (t, join))