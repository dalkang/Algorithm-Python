T = int(input())
 
for t in range(1, T+1):
    scores = list(map(int, input().split()))
    r = len(scores)
    total = 0
    
    for s in range(r):
        if scores[s] < 40:
            total += 40
        else:
            total += scores[s]
 
    print("#%d %d" % (t, total//r))