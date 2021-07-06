T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A_result = P * W
    B_result = 0
    
    if W > R:
        B_result = Q + (S * (W-R))
    elif W <= R:
        B_result = Q
     
    print("#%d %d" % (t, min(A_result, B_result)))