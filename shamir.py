import random
import itertools
from math import ceil

MAX_COEFF = 10**4

SHARES = 5
MIN_RECONSTRUCT = 3
SECRET = 614
PRIME = 655370000


def reconstruct_secret(shares):
    sums = 0
    mod = shares[0][2]
    for i, share_i in enumerate(shares):
        if share_i[2] != mod:
            return -1

    # print(f'Found mod = {mod}')

    for i, share_i in enumerate(shares):
        xi, yi, _ = share_i
        prod = 1.0
        for j, share_j in enumerate(shares):
            xj, _, _ = share_j
            if i != j:
                # print(f'xj = {xj}, xi = {xi}')
                # print(f'rownanie {i} to {xj / (xj - xi)}')
                prod *= (xj / (xj - xi))

        print(f'Iloczyn równań to {prod}')
        prod *= yi
        print(f'partial product = {prod}, modulo = {prod % mod}, bo yi = {yi}')
        sums += prod

    print(f'Sums = {sums}, sums%mod = {sums % mod}\n')
    return ceil(sums % mod)


def find_x(x, polynom):
    value = 0
    max_power = len(polynom)-1
    for j in range(len(polynom)):
        value += x**(max_power-j) * polynom[j]
        # print(f'{x} to the power of {max_power-j} is {x**(max_power-j)}, times {polynom[j]} is {x**(max_power-j) * polynom[j]}')

    # print(f'The total is {value}')
    # print(f'Sanity check: {value - (x**2 *polynom[0]) - (x*polynom[1])}')
    return value


def generate_polynomial(t, secret):
    coeff = []
    for i in range(t-1):
        coeff.append(random.randrange(0, MAX_COEFF))
    coeff.append(secret)
    return coeff


def generate_shares(n, m, secret, mod):
    """
    Generuje n udziałów sekretu secret, gdzie wystarczy m do jego odbudowania
    :param n: liczba generowanych udziałów
    :param m: threshold
    :param secret: sekret do podziału
    :return: zwraca listę udziałów
    """
    polynom = generate_polynomial(m, secret)
    print(f'Polynomial {polynom}')
    shares = []
    generated = []

    for i in range(1, n+1):
        # print("TERM", i)
        # print(find_x(i + 1, polynom))
        # print(find_x(i + 1, polynom) % mod)
        shares.append((i, (find_x(i, polynom) % mod), mod))

    return shares


if __name__ == "__main__":
    shares = generate_shares(SHARES, MIN_RECONSTRUCT, SECRET, PRIME)
    print(f'Wygenerowano udziały {shares}')
    for i in range(3):
        print(" ")
        pool = random.sample(shares, MIN_RECONSTRUCT)
        print(f'Na podstawie {pool}')
        recovered_secret = reconstruct_secret(pool)
        print(f'Odzyskano sekret {recovered_secret}')

    # attempts = 0
    # success = 0
    # bad_sets = []
    # perms = list(itertools.permutations(shares))
    # for i in range(len(perms)):
    #     attempts += 1
    #     if int(reconstruct_secret(perms[i][0:MIN_RECONSTRUCT])) == SECRET:
    #         success += 1
    #     else:
    #         bad_sets.append(perms[i][0:MIN_RECONSTRUCT])
    #
    # print(f'Tries: {attempts}, successes: {success}, rate {success/attempts*100}%')
    # print(bad_sets)
    # # for set in bad_sets:
    # #     numbers = []
    # #     for i in set:
    # #         numbers.append(i[0])
    # #     numbers.sort()
    # #     print(numbers)
    # #     print("===")
