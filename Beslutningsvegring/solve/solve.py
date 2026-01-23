import json
from pathlib import Path
from typing import List, Tuple

N = 256            
Q = 3329           
ETA = 3            
K = 2              

def eval_at_one(coeffs):
    return sum(coeffs) % Q

def load_samples(path):
    with open(path, "r") as fin:
        data = json.load(fin)
    samples = []
    for samp in data["samples"]:
        samples.append((samp["A"], samp["t"]))
    return samples

SMALL_INTERVAL = range(-ETA * N, ETA * N + 1)
THRESHOLD = Q // 6                             # 832

def guess_s1(samples):
    best_score, best_pair = -1, (0, 0)
    a1_rows = []
    t1_vecs = []
    for A, t in samples:
        a_vec = [eval_at_one(poly) for row in A for poly in row]
        t_vec = [eval_at_one(poly) for poly in t]
        a1_rows.append(a_vec)
        t1_vecs.append(t_vec)

    for s0 in SMALL_INTERVAL:
        for s1 in SMALL_INTERVAL:
            score = 0
            for a_vec, t_vec in zip(a1_rows, t1_vecs):
                val0 = (t_vec[0] - (a_vec[0] * s0 + a_vec[1] * s1)) % Q
                val1 = (t_vec[1] - (a_vec[2] * s0 + a_vec[3] * s1)) % Q
                if val0 > Q//2:
                    val0 -= Q
                if val1 > Q//2:
                    val1 -= Q
                if abs(val0) < THRESHOLD and abs(val1) < THRESHOLD:
                    score += 1
            if score > best_score:
                best_score, best_pair = score, (s0 % Q, s1 % Q)
                print(f"[*] New best score {score} with (s0,s1)={(s0,s1)}")
    return best_pair

def recover_bits(samples: list, s01: Tuple[int, int]) -> str:
    bits = []
    s0, s1 = s01
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

def bits_to_ascii(bitstr: str) -> str:
    l = len(bitstr)
    if l % 8 != 0:
        bitstr = bitstr[:l - (l % 8)]
    b = int(bitstr, 2).to_bytes(len(bitstr)//8, byteorder='big')
    try:
        return b.decode()
    except UnicodeDecodeError:
        return repr(b)

def main(json_path):
    samples = load_samples(json_path)
    print(f"Loaded {len(samples)} samples … guessing secret …")
    s01 = guess_s1(samples)
    print(f"[*] Likely s(1) values: {s01}")
    bits = recover_bits(samples, s01)
    print(f"Recovered {len(bits)} bits")
    flag = bits_to_ascii(bits)
    print(f"Flag: {flag}")

if __name__ == "__main__":
    path = r"Beslutningsvegring\output.json"
    main(path)
