for t in range(10):
    T = int(input())
    arr = list(map(int, input().split()))
    i = 0
    while arr[-1] != 0:
        if i == 5:
            i = 0
        arr[0] -= 1 + i
        if arr[0] < 0:
            arr[0] = 0
        for k in range(len(arr)-1):
            arr[k], arr[k-1] = arr[k-1], arr[k]
        i += 1
    print("#%d" % (T), *arr)