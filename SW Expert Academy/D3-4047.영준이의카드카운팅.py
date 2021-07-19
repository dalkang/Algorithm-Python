T = int(input())
 
for t in range(T):
    num = input()
    arr = [[0 for _ in range(13)] for _ in range(4)]
     
    for i in range(0, len(num), 3):
        if num[i] == 'S':
            r = 0
        elif num[i] == 'D':
            r = 1
        elif num[i] == 'H':
            r = 2
        elif num[i] == 'C':
            r = 3
        arr[r][int(num[i+1:i+3])-1] += 1
 
    for i in range(0, 4):
        if 2 in arr[i]:
            print("#%d %s" % (t+1, 'ERROR'))
            break
    else:
        a = 13 - sum(arr[0])
        b = 13 - sum(arr[1])
        c = 13 - sum(arr[2])
        d = 13 - sum(arr[3])
 
        print("#%d %d %d %d %d" % (t+1, a, b, c, d))