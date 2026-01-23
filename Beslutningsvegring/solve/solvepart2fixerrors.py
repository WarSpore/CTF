from typing import List, Tuple
import json

Q = 3329  

THRESHOLD = Q // 40   
print(THRESHOLD)
def eval_at_one(coeffs):
    return sum(coeffs) % Q


def recover_bits(samples):
    bits = []
    s0, s1 = (3279, 35)
    for A, t in samples:
        a_vec = [eval_at_one(poly) for row in A for poly in row]
        t_vec = [eval_at_one(poly) for poly in t]
        val0 = (t_vec[0] - (a_vec[0] * s0 + a_vec[1] * s1)) % Q
        val1 = (t_vec[1] - (a_vec[2] * s0 + a_vec[3] * s1)) % Q
        if val0 > Q//2: 
            val0 -= Q
        if val1 > Q//2:
            val1 -= Q
        both_small = abs(val0) < THRESHOLD and abs(val1) < THRESHOLD
        bits.append('0' if both_small else '1')
    return ''.join(bits)

def load_samples(path):
    with open(path, "r") as fin:
        data = json.load(fin)
    samples = []
    for samp in data["samples"]:
        samples.append((samp["A"], samp["t"]))
    return samples

json_path = r"Beslutningsvegring\output.json"

def bits_to_ascii(bitstr: str) -> str:
    l = len(bitstr)
    if l % 8 != 0:
        bitstr = bitstr[:l - (l % 8)]
    b = int(bitstr, 2).to_bytes(len(bitstr)//8, byteorder='big')
    try:
        return b.decode()
    except UnicodeDecodeError:
        return repr(b)

samples = load_samples(json_path)
bits = recover_bits(samples)
print(bits_to_ascii(bits))

