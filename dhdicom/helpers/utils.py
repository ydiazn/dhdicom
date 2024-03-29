

import hashlib
import math
import numpy as np


def md5_to_key_bin(key):
    hexa_data = hashlib.md5(key.encode('utf-8')).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)


def md5_to_image_bin(imag):
    hexa_data = hashlib.md5(imag).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)


def sha256_to_key_bin(key):
    hexa_data = hashlib.sha256(key.encode('utf-8')).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)[:256]


def sha256_to_image_bin(imag):
    hexa_data = hashlib.sha256(imag).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)[:256]


def sha512_to_key_bin(key):
    hexa_data = hashlib.sha512(key.encode('utf-8')).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)[:512]


def blake2b_bin(key):
    hexa_data = hashlib.blake2b(key.encode('utf-8')).hexdigest()
    return "".join(format(ord(x), '08b') for x in hexa_data)


def pwlcm(x, p):
    if x >= 0 and x < p:
        return x / p
    elif x >= p and x < 0.5:
        return (x - p) / (0.5 - p)
    elif x >= 0.5 and x < 1:
        return pwlcm(1 - x, p)


def chaotic_map(x, p, n):
    L = []
    for i in range(n):
        x = pwlcm(x, p)
        L.append(int(math.floor(x * 10 ** (14) % n)))
    return L


def perm(L, ind):
    pos = []
    n = len(ind)
    for i in range(n):
        pos.append(L[ind[i]])
    return pos


def set_diff(L1, L2):
    n = len(L2)
    for i in range(n):
        L1.remove(L2[i])
    return L1


def list_reduced(L):
    R = []
    for i in L:
        if i not in R:
            R.append(i)
    return R


def random_list(x, p, L):
    pos = []
    ind = []
    ind = list_reduced(chaotic_map(x, p, len(L)))
    pos = perm(L, ind)
    if len(pos) == len(L):
        return pos
    elif len(pos) == 1:
        return L
    else:
        return pos + random_list(x, p, set_diff(L, pos))
    return pos


def contracted_key(bin_seq, n=128):
    cad = ""
    L = []
    if list(bin_seq).count("1") == n:
        return bin_seq
    elif list(bin_seq).count("1") > n:
        for i in range(len(bin_seq)):
            if i not in L and list(cad).count("1") != n:
                cad += bin_seq[i]
    else:
        print("Error: Bits equal to 1 are not enough")
    return cad


# x e y are a list of integer numbers
# bin_seq is a binary sequence
def chaotic_positions(x, y, bin_seq):
    L = []
    x_chaotic_pos = [
        x[i] for i in range(len(x)) if i < len(bin_seq) and bin_seq[i] == "1"]
    L.append(x_chaotic_pos)
    y_chaotic_pos = [
        y[i] for i in range(len(y)) if i < len(bin_seq) and bin_seq[i] == "1"]
    L.append(y_chaotic_pos)
    return L


def chaotic_permutation(x, hash_key):
    n = len(hash_key)
    chaotic_perm = [x[i] for i in range(n) if hash_key[x[i]] == "1"]
    chaotic_perm += [x[i] for i in range(n) if hash_key[x[i]] == "0"]
    return chaotic_perm


def replace(byte_init, bit):
    if bit == '0':
        if byte_init % 2 == 0:
            byte_fin = byte_init
        else:
            byte_fin = byte_init - 1
    elif bit == '1':
        if byte_init % 2 == 0:
            byte_fin = byte_init + 1
        else:
            byte_fin = byte_init
    return byte_fin


def ext_lsb(byte):
    if byte % 2 == 0:
        return '0'
    return '1'


def or_operation(x, y):
    if len(x) == len(y):
        n = len(x)
        return "".join(("0" if x[i] == y[i] else "1") for i in range(n))
    else:
        print("It is not possible to perform this operation")


def multiply_matrix(A, B, C):
    if C != []:
        return np.dot(np.dot(A, B), C)
    else:
        return np.dot(A, B)


def increase_string(seq, n):
    cad = ""
    while len(cad) < n:
        cad += seq
    return cad[:n]


def char2bin(data):
    return "".join(format(ord(x), '08b') for x in data)


def bin2char(bin_seq):
    return ''.join(
        (chr(int(bin_seq[i:i+8], 2)) for i in range(0, len(bin_seq), 8))
    )


def list_min(vect, n):
    return np.asarray(sorted(vect.tolist())[:n])


def blake2b_bin_exp(key, n):
    cad = ""
    while len(cad) < n:
        hexa_data = hashlib.blake2b(key.encode('utf-8')).hexdigest()
        cad += "".join(format(ord(x), '08b') for x in hexa_data)
        key = bin2char(cad[-128:])
    return cad[:n]


def sha256_bin_exp(key, n):
    cad = ""
    while len(cad) < n:
        hexa_data = hashlib.sha256(key.encode('utf-8')).hexdigest()
        cad += "".join(format(ord(x), '08b') for x in hexa_data)
        key = bin2char(cad[-128:])
    return cad[:n]


def matrix2vector(A):
    L = []
    for i in range(len(A)):
        L.extend(A[i, :])
    return L


def vector2matrix(vect, n):
    m = len(vect) // n
    dims = (m, n)
    M = np.zeros(dims)
    for i in range(m):
        j = i * n
        k = (i + 1) * n
        M[i][:] = vect[j:k]
    return M


def gaussian_noise(B, m=8, n=8):
    import random
    if len(B.shape) == 2:
        for i in range(m):
            for j in range(n):
                altera_valor= random.uniform(1, 15)
                suma_or_resta = random.randint(0, 1)
                if suma_or_resta == 0:
                    B[i][j] = int(B[i][j]+altera_valor)
                else:
                    B[i][j] = int(B[i][j]-altera_valor)
    else:
        for i in range(m):
            for j in range(n):
                [r, g, b] = B[i][j][:]
                altera_valor= random.uniform(1, 15)
                suma_or_resta = random.randint(0, 1)
                if suma_or_resta == 0:
                    B[i][j][:] = [
                        int(r+altera_valor),
                        int(g+altera_valor),
                        int(b+altera_valor)
                    ]
                else:
                    B[i][j][:] = [
                        int(r-altera_valor),
                        int(g-altera_valor),
                        int(b-altera_valor)
                    ]
    return B


def sp_noise(B, prob, m=8, n=8):
    import random
    if len(B.shape) == 2:
        for i in range(m):
            for j in range(n):
                if random.random() < prob:
                    sal_p = random.randint(0, 1)
                    if sal_p == 0:
                        sal_p = 0
                    else:
                        sal_p = 255
                    B[i][j] = sal_p
    else:
        for i in range(m):
            for j in range(n):
                [r, g, b] = B[i][j][:]
                if random.random() < prob:
                    sal_p = random.randint(0, 1)
                    if sal_p == 0:
                        sal_p = 0
                    else:
                        sal_p = 255
                    B[i][j][:] = [sal_p, sal_p, sal_p]
    return B


def cropping_noise(B, m=8, n=8):
    if len(B.shape) == 2:
        for i in range(m):
            for j in range(n):
                B[i][j] = 0
    else:
        for i in range(m):
            for j in range(n):
                B[i][j][:] = 0
    return B


def increase_list(seq, n):
    L = []
    while len(L) < n:
        L.extend(seq)
    return L[:n]


def half_key(key):
    return or_operation(key[:128], key[128:])


def list2str(L):
    return "".join(str(i) for i in L)


def base_change(entrada, base, n=None):
    r = []
    pe = 1
    while pe != 0:
        pe = entrada // base
        r.insert(0, entrada % base)
        entrada = pe
    if n == None:
        return list2str(r)
    elif len(r) == n:
        return list2str(r)
    elif len(r) > n:
        return list2str(r[-n:])
    else:
        m = n - len(r)
        for i in range(m):
            r.insert(0, 0)
        return list2str(r)


def bin2dec(bin_seq):
    dec_repr = 0
    for i in range(len(bin_seq)):
        if bin_seq[len(bin_seq) - i - 1] != '0':
            dec_repr += 2 ** i
    return dec_repr


def embedded_size(n, nblocks):
    res = n % 256
    if res == 0:
        m = n // 256
        L = [512 for i in range(m)]
    else:
        m = (n - res) // 256
        L = [512 for i in range(m)]
        L.append(256 + res)
    nblocks -= len(L)
    L.extend([256 for i in range(nblocks)])
    return L
