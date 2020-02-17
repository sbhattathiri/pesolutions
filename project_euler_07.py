import math


def is_prime(n):
    square_root = int(math.sqrt(n))
    for i in range(2,square_root+1):
        if n%i == 0:
            return False
    else:
        return True

def count_primes(max):
    i = 0
    num = 2
    while i < max:
        if is_prime(num):
            i = i + 1
            prime_num = num
        num = num + 1
    return prime_num


if __name__ == '__main__':
    print(count_primes(6))