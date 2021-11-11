a = int(input())
if a == 0:
    print(0)
else:
    fib_p, fib_n = 0, 1
    n = 1
    while fib_n <= a:
        if fib_n == a:
            print(n)
            break
        fib_p, fib_n = fib_n, fib_p + fib_n
        n += 1
    else:
        print(-1)