
def fib_skonczony(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fib_nieskonczony():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    fib_skonczony(10)
    for liczba in fib_skonczony(10):
        print(liczba, end=" ")
    print()

    gen = fib_nieskonczony()
    
    for _ in range(10):
        liczba = next(gen)
        print(liczba, end=" ")
    print()

    for _ in range(10):
        liczba = next(gen)
        if liczba % 3 == 0:
            print(liczba, end=" ")
    print()

    for _ in range(10):
           liczba = next(gen)
           if liczba % 5 == 0:
               print(liczba, end=" ")
    print()


main()