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
    while not (x != y and x % 4 == 3 and y % 4 == 3):
        x = sample(primes, 1)[0]
        y = sample(primes, 1)[0]
    return x, y


def bbs_generator(len, N, min=MIN, max=MAX):
    random_string = ""
    x = randrange(min, max)
    while gcd(N, x) != 1:
        x = randrange(min, max)
    for i in range(len):
        x = (x ** 2) % N
        random_string = random_string + str(x % 2)
    return random_string


def counter_test(string):
    if 10275 > string.count("1") > 9725:
        return True
    else:
        return False


def series_test_engine(string):
    counter = 0
    s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
    for i in range(len(string)):
        if string[i] == "0":
            counter += 1
        else:

            if counter == 1:
                s1 += 1
            elif counter == 2:
                s2 += 1
            elif counter == 3:
                s3 += 1
            elif counter == 4:
                s4 += 1
            elif counter == 5:
                s5 += 1
            elif counter > 5:
                s6 += 1
            counter = 0

    return s1, s2, s3, s4, s5, s6


def series_test(string):
    s1, s2, s3, s4, s5, s6 = series_test_engine(string)
    result = True
    if not 2315 < s1 < 2685:
        result = False
    if not 1114 < s2 < 1386:
        result = False
    if not 527 < s3 < 723:
        result = False
    if not 240 < s4 < 384:
        result = False
    if not 103 < s5 < 209:
        result = False
    if not 103 < s6 < 209:
        result = False

    return result


def long_series_test_engine(string):
    max_len = 0
    last_char = string[0]
    counter = 1
    for i in range(1, 20000):
        if string[i] == last_char:
            counter += 1
        else:
            last_char = string[i]
            if max_len < counter:
                max_len = counter
            counter = 0
    return max_len


def long_series_test(string):
    return True if long_series_test_engine(string) < 26 else False


def convert_from_binary(string):
    msb = len(string) - 1
    ret = 0
    for i, bit in enumerate(string):
        if not (bit == "0" or bit == "1"):
            raise ValueError("Provided string did not contain only zeroes and ones")
        ret += int(bit) * (2**(msb-i))
    return ret


def poker_test_engine(string):
    ret = {}
    if len(string) % 4 != 0:
        raise ValueError("długość ciągu powinna być podzielna przez 4")
    for i in range(0, len(string), 4):
        decimal = str(convert_from_binary(string[i:i+4]))
        if decimal not in ret:
            ret[decimal] = 1
        else:
            ret[decimal] += 1
    return ret


def poker_test(string):
    wdict = poker_test_engine(string)
    inter_value = 0
    for value in wdict.values():
        inter_value += value*value
    test_result = 16/5000 * inter_value - 5000
    return True if 2.16 < test_result < 46.17 else False


def run_all_tests(string):
    ret = True
    if len(string) < 20000:
        raise ValueError("Testy statystycznie nie są skuteczne dla ciągów krótszych od 20000 bitów")
    if len(string) > 20000:
        print("Testy zostały przygotowane dla ciągów o długości 20000, użyto pierwszych 20000 bitów danego ciągu")
        string = string[:20000]
        print(len(string))
    if not counter_test(string):
        print("Failed counter test")
        ret = False
    if not series_test(string):
        print("Failed series test")
        ret = False
    if not long_series_test(string):
        print("Failed long series test")
        ret = False
    if not poker_test(string):
        print("Failed poker test")
        ret = False
    return ret


if __name__ == "__main__":
    # p, q = generate_primes(MIN, MAX)
    p = 8730841139
    q = 6749341223
    N = p * q
    print(f"p = {p}, q = {q}, N = {N}")
    for i in range(100):
        rand_string = bbs_generator(20000, N)
        result = run_all_tests(rand_string)
        print(result)
        if not result:
            print(f"Counter test raw: {rand_string.count('1')}")
            print(f"Series test raw result: {series_test_engine(rand_string)}")
            print(f"Long series test raw result: {long_series_test_engine(rand_string)}")
            print(f"Poker test raw result: {poker_test_engine(rand_string)}")
