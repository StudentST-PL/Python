"""
class Parzyste:
    def __init__(self, limit=None):
        self.limit = limit
        self.licznik = 0
        self.aktualna = 2
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.limit is not None and self.licznik >= self.limit:
            raise StopIteration
        
        wynik = self.aktualna
        self.aktualna += 2
        self.licznik += 1
        return wynik
    
for x in Parzyste(3):
    print(x)

it = Parzyste()
print(next(it))
print(next(it))
"""

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
    Fibonacci(10)
  
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