T = int(input())
 
for t in range(1, T+1):
    print("#%d" % (t), end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    cnt1 = 0
    cnt1_lst = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[x][y] != 0:
                cnt1 += 1
            else:
                if cnt1 != 0:
                    cnt1_lst.append(cnt1)
                cnt1 = 0
 
    dic = {}
    for i in cnt1_lst:
        dic[i] = dic.get(i, 0) + 1
    print("%d" % (len(dic)), end=' ')
     
    result = []
    for keys, values in dic.items():
        result.append([keys, values, keys*values])
    result_sort = sorted(result, key = lambda x : x[2])
 
    for r in range(len(result_sort)):
        print(result_sort[r][0], result_sort[r][1], end=' ')
    print()