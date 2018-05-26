def fib(n):
    result = [0, 1]
    a = 0
    b = 1
    c = 0
    # print a,b,
    while (c < n):
        c = a + b
        a = b
        b = c
        # print c,
        result.append(c)
    else:
        print 'done.'
        return result


a = fib(100)

print a
