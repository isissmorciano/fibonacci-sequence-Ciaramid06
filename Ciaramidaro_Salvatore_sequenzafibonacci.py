# Implementazione iterativa
def iterativo_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        # Inizializza i primi due numeri della successione
        fib_0 = 0
        fib_1 = 1
        # Calcola i successivi numeri della successione fino al numero desiderato
        for i in range(2, n+1):
            fib_i = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib_i
        return fib_i

# Implementazione ricorsiva
def ricorsiva_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return ricorsiva_fibonacci(n-1) + ricorsiva_fibonacci(n-2)
    

# Input
n = int(input("Inserisci l'indice n della successione di Fibonacci: "))

# Output
print("Funzione iterativa di Fibonacci:", iterativo_fibonacci(n))
print("Funzione ricorsiva di Fibonacci:", ricorsiva_fibonacci(n))
