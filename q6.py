def is_prime(m):
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

def separate(A, n, nonprime, prime):
    for j in range(n):
        if is_prime(A[j]):
            prime.append(A[j])
        else:
            nonprime.append(A[j])
    return nonprime, prime

def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nonprime = []
    prime = []
    nonprime, prime = separate(A, len(A), nonprime, prime)
    print("The final result after separation is:\n", "Non-primes:", nonprime, "\nPrimes:", prime)

if __name__ == "__main__":
    main()
