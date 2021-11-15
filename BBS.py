from random import randrange, sample
from sympy import isprime, primerange
from math import gcd

MIN = 1000000
MAX = 10000000


def generate_primes(min, max):
    primes = list(primerange(min, max))
    # print(primes)
    x = sample(primes, 1)[0]
    y = sample(primes, 1)[0]
    while not(x!=y and x%4==3 and y%4==3):
        x = sample(primes, 1)[0]
        y = sample(primes, 1)[0]
    return x, y


def bbs_generator(len, N,  min = MIN, max = MAX):
    random_string = ""
    x = randrange(min, max)
    while gcd(N, x) != 1:
        x = randrange(min, max)
    for i in range(len):
        x = (x**2) % N
        random_string = random_string + str(x%2)
    return random_string


def counter_test(string):
    if 10275 > string.count("1") > 9725:
        return True
    else:
        print(f'Amount of 1 was {string.count("1")}')
        return False


def series_test(string):
    counter = 0
    s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
    for i in range(len(string)):
        if string[i] == "0":
            counter += 1
        else:

            if counter == 1:
                s1 += 1
            elif counter == 2:
                s2 +=1
            elif counter == 3:
                s3 +=1
            elif counter == 4:
                s4 +=1
            elif counter == 5:
                s5 +=1
            elif counter > 5:
                s6 +=1
            counter = 0

    return (s1,s2,s3,s4,s5,s6)

def long_series_test(string): #TODO: naprawić
    max_len = 0
    last_char = string[0]
    counter = 1
    for i in range(1, 20000):
        if string[i] == last_char:
            counter += 1
        else:
            last_char = string[i]
            if max_len > counter:
                max_len = counter
            counter = 0
    return max_len


if __name__ == "__main__":
    # p, q = generate_primes(MIN, MAX)
    p = 8730841139
    q = 6749341223
    N = p*q
    print(p, q, N)
    rand_string = bbs_generator(20000, N)
    print(rand_string)
    print(counter_test(rand_string))
    print(series_test(rand_string))
    print(long_series_test(rand_string))


