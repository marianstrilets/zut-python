

'''
Napisz program, który znajdzie i wy±wietli n pierwszych liczb pierwszych 
(zakładając, że pierwszą liczbą pierwszą jest liczba 2) .

'''

primes = [2]
x = 2
n=7
while len(primes) < n:
    x += 1
    isPrime = True
    for i in range(2, x):
        if x % i == 0:
            isPrime = False
            break
        if isPrime:
            primes.append(x)
print(primes)