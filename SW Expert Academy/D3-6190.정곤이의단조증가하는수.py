T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    Numbers = list(map(int, input().split()))
    max_number = []

    for n in range(N-1):
        for o in range(n+1, N):
            mid_list = []
            mid = Numbers[n] * Numbers[o]
            for p in str(mid):
                mid_list.append(p)
            for q in range(len(mid_list)-1):
                if mid_list[q] > mid_list[q+1]:
                    break
                else:
                    if q == len(mid_list)-2:
                        max_number.append(mid)
                        
    if len(max_number) == 0:
        print("#%d" % (t),'-1')
    else:
        print("#%d" % (t), max(max_number))