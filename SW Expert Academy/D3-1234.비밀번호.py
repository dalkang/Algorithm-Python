for T in range(10):
    print("#%d" % (T+1), end=' ')
    
    length, number = input().split()
    numbers = list(number)
 
    while True:
        a = len(numbers)
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                for _ in range(2):
                    numbers.pop(i)
                break
        b = len(numbers)
        if a == b:
            break
 
    for n in numbers:
        print(n, end='')
    print()