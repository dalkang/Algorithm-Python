T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
 
    for n in range(N):
        for nn in range(N):
            if N_list[n] < N_list[nn]:
                N_list[n], N_list[nn] = N_list[nn], N_list[n]
 
    print("#%d" % (t), *N_list)