from math import gcd
from sympy import isprime

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r

a = -15031320841187090205796125674696580906358618345270457325350277971483199628722232374974653720650852722122083001446931346096957820111721436460470382584719144314669385718634267413303766147037844448829668250145567253908858196379611295193721263377435120489141356119720208099989000277736130324935940276821727190650
b = 21163038100504353557309818489479333035358731777847137577705531181160508032628726767683360746849641705779308539820874250835067943437038491479295081432101722933254893539909517286020941487294650069148219843915803833997393774938221902776933735566267165634712871741732788347665985115990416317619721742938262344837

if gcd(a, b) != 1:
    print("Error: a and b are not coprime, the equation will not have integer solutions.")
    exit()

p0, q0, gcd_ab = extended_gcd(a, b)
expected_bits = 1024
min_value = 2 ** (expected_bits - 1)
max_value = 2 ** expected_bits
k = 0
found = False

print("Searching for valid prime (p, q) pairs...")

while not found:
    for sign in [1, -1]:
        p = p0 + sign * k * b
        q = q0 - sign * k * a
        if min_value <= abs(p) <= max_value and min_value <= abs(q) <= max_value:
            if isprime(abs(p)) and isprime(abs(q)):
                print(f"\nFound valid primes after {k} attempts:")
                print(f"p = {abs(p)}")
                print(f"q = {abs(q)}")
                print(f"k = {sign * k}")
                found = True
                break

    if not found:
        k += 1
