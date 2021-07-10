T = int(input())
 
for t in range(1, T+1):
    N, K = map(int, input().split())
    K_list = list(map(int, input().split()))
    n_list = []

    for n in range(1, N+1):
        if n not in K_list:
            n_list.append(n)
            
    print("#%d" % (t), *n_list)