#!/usr/bin/env python3
from pwn import *
import re
import sys
from collections import Counter
from string import ascii_uppercase

EN_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
    0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929,
    0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
    0.01974, 0.00074
]

AZ = ascii_uppercase
A2I = {c:i for i,c in enumerate(AZ)}

def rot_counts(counts, shift):
    """Rotate counts (list of 26 ints) by 'shift' to model decrypt shift."""
    shift %= 26
    return counts[-shift:] + counts[:-shift] if shift else counts[:]

def chi_squared(observed_counts, sample_size):
    """Chi-squared against English expectation for a single Caesar column."""
    exp = [sample_size * f for f in EN_FREQ]
    s = 0.0
    for o, e in zip(observed_counts, exp):
        if e > 0:
            d = o - e
            s += (d * d) / e
    return s

def best_shift_for_column(col_text):
    n = len(col_text)
    if n == 0:
        return 0, float('inf')

    cnt = [0]*26
    for ch in col_text:
        cnt[A2I[ch]] += 1

    best_s, best_score = None, float('inf')
    for s in range(26):
        rotated = rot_counts(cnt, -s)
        score = chi_squared(rotated, n)
        if score < best_score:
            best_s, best_score = s, score
    return best_s, best_score


def crack_vigenere(ct, min_k=4, max_k=7):
    """
    Recover key (length between min_k and max_k) and plaintext for a given ciphertext.
    Returns (key, plaintext).
    """
    ct = ''.join(c for c in ct if c in AZ)
    best_total, best_key = float('inf'), None
    best_pt = None

    for k in range(min_k, max_k+1):
        shifts = []
        total_score = 0.0
        for i in range(k):
            col = ct[i::k]
            s, sc = best_shift_for_column(col)
            shifts.append(s)
            total_score += sc

        key = ''.join(AZ[s] for s in shifts)
        pt_chars = []
        for idx, ch in enumerate(ct):
            s = shifts[idx % k]
            p = (A2I[ch] - s) % 26
            pt_chars.append(AZ[p])
        pt = ''.join(pt_chars)

        if total_score < best_total:
            best_total = total_score
            best_key = key
            best_pt = pt

    return best_key, best_pt

def solve_session(io):
    io.recvuntil(b"Are you ready?")
    io.sendline(b"yes")

    round_no = 0
    while True:
        line = io.recvline(timeout=10)
        if not line:
            log.failure("Connection closed.")
            break

        if b"Here is some ciphertext" in line:
            ct = io.recvline().decode().strip()
            a = io.recvuntil(b"> ")
            key, pt = crack_vigenere(ct, 4, 7)
            io.sendline(pt.encode())
            resp = io.recvline(timeout=10)
            if not resp:
                log.failure("No response after submitting plaintext.")
                break
            if b"That is correct" in resp:
                round_no += 1
                log.success(f"Round {round_no} solved (key guessed: {key})")
                continue
            elif b"That is not correct" in resp:
                log.failure(resp.decode().strip())
                break
        elif b"Very good here is a flag as a reward" in line:
            flag = io.recvline(timeout=5).decode().strip()
            print(flag)
            break
        else:
            continue

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] != "-":
        host = sys.argv[1]
        port = int(sys.argv[2])
        io = remote(host, port)
    else:
        print("Usage for remote: ./solve.py <host> <port>")
        sys.exit(0)

    try:
        solve_session(io)
    finally:
        io.close()
