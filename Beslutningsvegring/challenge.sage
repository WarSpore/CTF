import os
import json

with open("flag.txt", "r") as fin:
    flag = fin.read().strip().encode()

assert flag.decode().isprintable()


def sample_poly_cbd(Rq, n, q, eta):
    coeffs = [0] * n
    num_bits = n * 2 * eta
    b = int.from_bytes(os.urandom(num_bits // 8), "big")
    bits = [0] * num_bits

    for i in range(num_bits):
        bits[i] = b & 1
        b >>= 1

    for i in range(n):
        x = sum(bits[2*i*eta : (2*i + 1)*eta])
        y = sum(bits[(2*i + 1)*eta : (2*i + 2)*eta])
        coeffs[i] = x - y

    return Rq(coeffs)


def sample_poly_uniform(Rq, n, q):
    coeffs = []

    while len(coeffs) < n:
        r = int.from_bytes(os.urandom(24 // 8), "big")
        r0 = (r >>  0) & 0xfff
        r1 = (r >> 12) & 0xfff

        if r0 < q:
            coeffs.append(r0)
        elif r1 < q:
            coeffs.append(r1)

    return Rq(coeffs[:n])


def gen_mlwe_sample(Rq, n, q, eta, k, s):
    A = matrix(Rq, [[sample_poly_uniform(Rq, n, q) for i in range(k)] \
                                                   for j in range(k)])
    e = vector(Rq, [sample_poly_cbd(Rq, n, q, eta) for _ in range(k)])
    t = A * s + e

    return (A, t)


def gen_uniform_sample(Rq, n, q, k):
    A = matrix(Rq, [[sample_poly_uniform(Rq, n, q) for i in range(k)] \
                                                   for j in range(k)])
    t = vector(Rq, [sample_poly_uniform(Rq, n, q) for _ in range(k)])

    return (A, t)


def samples_to_json(samples):
    samples_list = []

    for A, t in samples:
        A_list = [[list(map(int, a_ij)) for a_ij in row] for row in A]
        t_list = [list(map(int, t_i)) for t_i in t]
        samples_list.append({"A" : A_list, "t" : t_list})

    return json.dumps({"samples" : samples_list})


def samples_from_json(json_str, Rq):
    samples = []
    data = json.loads(json_str)

    for sample in data["samples"]:
        A_list = sample["A"]
        t_list = sample["t"]
        A = matrix(Rq, [[Rq(a_ij) for a_ij in row] for row in A_list])
        t = vector(Rq, [Rq(t_i) for t_i in t_list])
        samples.append((A, t))

    return samples


n = 256
q = 3329
eta = 3
k = 2

Rq.<x> = PolynomialRing(GF(q), names=["x"]).quotient(x^n - 1)
s = vector(Rq, [sample_poly_cbd(Rq, n, q, eta) for _ in range(k)])

flag_int = int.from_bytes(flag, byteorder="big")
flag_bits = bin(flag_int)[2:].zfill(8 * len(flag))

samples = []
for b in flag_bits:
    if b == '0':
        A, t = gen_mlwe_sample(Rq, n, q, eta, k, s)
    else:
        A, t = gen_uniform_sample(Rq, n, q, k)

    samples.append((A, t))

with open("output.json", "w") as fout:
    fout.write(samples_to_json(samples))
