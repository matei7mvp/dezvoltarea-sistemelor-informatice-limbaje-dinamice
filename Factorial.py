semn = lambda x : -1 if x < 0 else 1

def factorial(n):
    def factorial_recursiv(n):
        # 5! = 120
        # -5! = -120
        if n == 0:
            return 1
        else:
            return n * factorial_recursiv(n - 1)
    return semn(n) * factorial_recursiv(abs(n))

# print(factorial_recursiv(0))
# print(factorial_recursiv(5))
# print(factorial_recursiv(-5)) --> Eroare --> print(factorial_recursiv(abs(-5)) * semn(-5))

# print(factorial(-5))

print(factorial(int(input("N --> "))))
