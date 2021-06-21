T = int(input())
 
 
for i in range(T):
    n, m = list(map(int, input().split()))
    result = ''
    if n > m:
        result = '>'
    elif n < m:
        result = '<'
    else:
        result = '='
 
    print("#%d %s" % (i+1, result))