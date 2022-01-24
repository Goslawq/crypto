import random
import sys
from math import gcd


def get_keys():
    p = 2399660514525610390276365929095219712165000877099201397187633003
    q = 4905261593349468834689617079375943300268369166175398913784118587
    n = p * q
    phi = (p - 1) * (q - 1)
    # print(n)
    # print(phi)
    e = random.randrange(2, 1000000000000000)
    while gcd(e, phi) != 1:
        e = random.randrange(2, 100000000000000)
    d = pow(e, -1, phi)
    return (e, n), (d, n)


def cipher(message, key):
    f, n = key
    return [pow(x, f, n) for x in message]


def encrypt(m, k):
    return cipher(bytes(m, 'utf-8'), k)


def decrypt(m, k):
    return bytes(cipher(m, k)).decode('utf-8')


if __name__ == "__main__":
    # print(get_keys())
    pub, priv = get_keys()
    secret_message = "Lorem ipsum dolor sit amet, consectetur cras amet."
    encrypted = encrypt(secret_message, pub)
    print(encrypted)
    decrypted = decrypt(encrypted, priv)
    print(decrypted)

