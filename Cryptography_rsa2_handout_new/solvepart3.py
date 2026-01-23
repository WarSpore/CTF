#!/usr/bin/env python3
import re
import math
from sympy import mod_inverse, nthroot_mod
from Crypto.Util.number import long_to_bytes

def parse_input_file(filename, num_entries=7):
    """
    Parses the input file and extracts the first num_entries RSA entries.
    Each entry is a dictionary containing:
      - N (modulus)
      - e (public exponent)
      - phi(N) (Euler's totient function)
      - factors (list of tuples (p, exp))
    """
    with open(filename, 'r') as f:
        content = f.read()
    entries = re.split(r'\nEntry \d+:', content)
    rsa_entries = []
    for entry in entries:
        entry_dict = {}
        lines = entry.strip().split("\n")
        for line in lines:
            if line.startswith("N ="):
                entry_dict["N"] = int(line.split("= ")[1])
            elif line.startswith("e ="):
                entry_dict["e"] = int(line.split("= ")[1])
            elif line.startswith("phi(N) ="):
                entry_dict["phiN"] = int(line.split("= ")[1])
            elif line.startswith("c ="):
                entry_dict["c"] = int(line.split("= ")[1])
            elif line.startswith("factors ="):
                factors_str = line.split("= ")[1]
                entry_dict["factors"] = eval(factors_str)  # list of (p, exp)
        if entry_dict:
            rsa_entries.append(entry_dict)
        if len(rsa_entries) == num_entries:
            break
    return rsa_entries

def extended_gcd(a, b):
    """Return (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

def combine_two(a1, m1, a2, m2):
    """
    Combine two congruences:
         x ≡ a1 (mod m1)
         x ≡ a2 (mod m2)
    using generalized CRT. Returns (x, M) where M is the lcm(m1, m2).
    """
    d = math.gcd(m1, m2)
    if (a1 - a2) % d != 0:
        raise ValueError(f"No solution exists: a1={a1}, a2={a2}, gcd={d}")
    m1_div = m1 // d
    m2_div = m2 // d
    diff = (a2 - a1) // d
    g, inv, _ = extended_gcd(m1_div, m2_div)
    t = (diff * inv) % m2_div
    x = a1 + t * m1
    M = (m1 * m2) // d
    return (x % M, M)

def chinese_remainder_theorem(remainders, moduli):
    """
    Combine a list of congruences using CRT.
    Returns (x, M) where M is the combined modulus.
    """
    if not remainders:
        raise ValueError("No congruences provided.")
    x, M = remainders[0], moduli[0]
    for i in range(1, len(remainders)):
        x, M = combine_two(x, M, remainders[i], moduli[i])
    return (x, M)

def selected_primes(factors, cutoff=1e8):
    """
    From a list of (p, exp) pairs, return all primes p that are larger than cutoff.
    (We work with the base prime only.)
    """
    return [p for p, exp in factors if p > cutoff]

def collect_candidate_dict(entries):
    """
    For each RSA entry, for each selected prime p (p > cutoff) from its factorization,
    compute candidate residues as follows:
      - If gcd(e, phi(N)) == 1: compute candidate = (c^d mod p)
      - If gcd(e, phi(N)) == 2: compute e' = e/2, then d0 = mod_inverse(e', (p-1)//2),
        and let t = c^(d0) mod p, then solve nthroot_mod(t, 2, p, all_roots=True)
    Returns a dictionary mapping each prime p to a set of candidate residues.
    """
    cand_dict = {}
    for entry in entries:
        e_val = entry["e"]
        phiN = entry["phiN"]
        N_val = entry["N"]
        c_val = entry["c"]
        primes = selected_primes(entry["factors"], cutoff=50)
        if not primes:
            continue
        g_val = math.gcd(e_val, phiN)
        # Only handle gcd=1 and gcd=2 cases.
        if g_val not in (1, 2):
            continue
        for p in primes:
            try:
                if g_val == 1:
                    d = mod_inverse(e_val, p - 1)
                    cand = pow(c_val % p, d, p)
                    cand_dict.setdefault(p, set()).add(cand)
                elif g_val == 2:
                    e_prime = e_val // 2
                    d0 = mod_inverse(e_prime, (p - 1) // 2)
                    t = pow(c_val % p, d0, p)  # t should equal m^2 mod p.
                    roots = nthroot_mod(t, 2, p, all_roots=True)
                    for r in roots:
                        cand_dict.setdefault(p, set()).add(r)
            except Exception as ex:
                print(f"Skipping key for prime {p} due to error: {ex}")
                continue
    return cand_dict

def backtracking_crt(primes, candidate_lists, index=0, current_rem=None, current_mod=1):
    """
    Recursive backtracking to combine candidate residues.
    primes: list of primes
    candidate_lists: list of lists (each candidate_list[i] corresponds to candidates for primes[i])
    index: current index in primes to combine
    current_rem, current_mod: current CRT combined value and modulus.
    
    Returns a list of solutions as tuples (x, M).
    """
    if index == len(primes):
        return [(current_rem, current_mod)]
    solutions = []
    for candidate in candidate_lists[index]:
        try:
            if current_rem is None:
                new_rem, new_mod = candidate, primes[index]
            else:
                new_rem, new_mod = combine_two(current_rem, current_mod, candidate, primes[index])
            sols = backtracking_crt(primes, candidate_lists, index+1, new_rem, new_mod)
            solutions.extend(sols)
        except ValueError:
            continue
    return solutions

def main():
    # Read RSA entries.
    filename = "Cryptography_rsa2_handout_new\decryptable2.txt"  # Adjust path as needed
    num_entries = 64
    entries = parse_input_file(filename, num_entries=num_entries)
    if len(entries) < 2:
        print("Error: Not enough RSA entries found!")
        return

    # Test with a controlled message (e.g. "a" repeated i times).
    for i in range(930,931):
        # m_original = "a" * i
        # m = int.from_bytes(m_original.encode(), "big")
        # Encrypt with each RSA key using full modulus N.
        for entry in entries:
            entry["c"] = entry["c"]
        # Collect candidate residues for each prime.
        cand_dict = collect_candidate_dict(entries)
        if len(cand_dict) < 2:
            print(f"Message length {i}: Not enough candidate primes collected.")
            continue
        # Sort the primes and form candidate lists.
        sorted_primes = sorted(cand_dict.keys())
        candidate_lists = [sorted(list(cand_dict[p])) for p in sorted_primes]
        # print(f"Message length {i}: Trying backtracking CRT over primes: {sorted_primes}")
        solutions = backtracking_crt(sorted_primes, candidate_lists)
        solution_found = False
        for sol, mod in solutions:
            try:
                decoded = long_to_bytes(sol).decode("utf-8")
                print(f"Message length {i}")
                print("Decoded message:", decoded)
                solution_found = True
                break
            except Exception as e:
                continue
        if not solution_found:
            print(f"Message length {i}: No valid decoding found among {len(solutions)} combinations.")
        print("-" * 60)

if __name__ == "__main__":
    main()
