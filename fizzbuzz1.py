def fizzbuzz1():
    s3 = 0
    s5 = 0
    s15 = 0
    for n in range(1, 1000):
        n += 1
        if n % 3 == 0:
            s3 += n
        if n % 5 == 0:
            s5 += n
        if n % 15 == 0:
            s15 += n

    return (s3 + s5 - s15)

def fizzbuzz2():
    return sum(
        [n for n in range(1, 1000) if any(x == 0 for x in [n % div for div in (3, 5)])]
    )

def fizzbuzz3(dividers=None, N=1000):
    dividers = None or (3, 5)
    return sum(
        [n for n in range(1, N) if any(n % div == 0 for div in dividers)]
    )

def fizzbuzz4(*args, N=10000):
    return sum(
        n for n in range(1, N) if any(n % div == 0 for div in args)
    )
print(fizzbuzz1())
print(fizzbuzz2())
print(fizzbuzz3())
print(fizzbuzz4(3,5,7))