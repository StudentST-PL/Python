class Fibonacci:
    def __init__(self, n=None):
        self.n = n
        self.a = 1
        self.b = 1
        self.licznik = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.n is not None and self.licznik >= self.n:
            raise StopIteration

        wynik = self.a
        self.a, self.b = self.b, self.a + self.b
        self.licznik += 1
        return wynik

def main():
    for liczba in Fibonacci(10):
        print(liczba, end=" ")
    print()

    gen = Fibonacci()
    
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