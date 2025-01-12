import numpy as np
from numpy.polynomial import Polynomial as P

# Parameters
q = 65575  # Modulus
n = 256   # Degree of cyclotomic polynomial (for simplicity we use Φ(x) = x^n - 1)
b_bound = 65575  # Bound for small polynomials (e.g., s(x), e_i(x))

# Function to sample a random polynomial with coefficients in F_q
def random_polynomial(degree, modulus):
    # Coefficients are drawn uniformly from 0 to q-1
    coefficients = np.random.randint(0, modulus, degree)
    return P(coefficients)

# Function to sample a small random polynomial (error or secret) with coefficients following a Gaussian distribution
def gaussian_polynomial(degree, bound, modulus):
    # Coefficients are drawn from a Gaussian distribution
    coefficients = np.random.normal(0, bound, degree).astype(int)
    # Ensure coefficients are in F_q (non-negative and less than modulus)
    coefficients = np.mod(coefficients, modulus)
    print(coefficients)
    return P(coefficients)

# Function to perform polynomial multiplication and reduce coefficients modulo q
def mod_polynomial(poly, modulus):
    # Ensure coefficients are in F_q (mod q)
    mod_coefficients = np.mod(poly.coef, modulus)
    return P(mod_coefficients)

# Generating the known polynomials a_i(x)
def generate_a_polynomials(num_polynomials, degree, modulus):
    return [random_polynomial(degree, modulus) for _ in range(num_polynomials)]

# Generate the secret polynomial s(x)
def generate_secret_polynomial(degree, bound, modulus):
    return gaussian_polynomial(degree, bound, modulus)

# Generate the error polynomials e_i(x)
def generate_error_polynomials(num_polynomials, degree, bound, modulus):
    return [gaussian_polynomial(degree, bound, modulus) for _ in range(num_polynomials)]

# Generate random b_i(x) polynomials (without using s(x))
def generate_random_b_polynomials(num_polynomials, degree, modulus):
    return [random_polynomial(degree, modulus) for _ in range(num_polynomials)]

def reduce_degree(poly, degree):
    # Ensure the polynomial degree does not exceed n-1 (mod x^n - 1)
    mod_coefficients = np.mod(poly.coef[:degree], q)
    return P(mod_coefficients)

# Main RLWE Decision problem data generation function
def generate_rlwe_decision_data(num_polynomials, degree, modulus, bound):
    # Step 1: Generate known polynomials a_i(x)
    a_polynomials = generate_a_polynomials(num_polynomials, degree, modulus)
    
    # Step 2: Generate the secret polynomial s(x)
    s = generate_secret_polynomial(degree, bound, modulus)
    
    # Step 3: Generate small error polynomials e_i(x)
    error_polynomials = generate_error_polynomials(num_polynomials, degree, bound, modulus)
    
    # Step 4: Generate b_i(x) polynomials with two cases:
    # - With probability 50%, use RLWE relation
    # - Otherwise, generate a random polynomial
    b_polynomials = []
    labels = []  # 1 if b_i(x) is RLWE, 0 if b_i(x) is random
    for i, (a, e) in enumerate(zip(a_polynomials, error_polynomials)):
        if np.random.rand() < 0.5:
            # RLWE construction with degree reduction
            product = a * s
            product_mod_q = mod_polynomial(product, modulus)
            product_mod_q_reduced = reduce_degree(product_mod_q, degree)  # Ensure degree <= n-1
            b = product_mod_q_reduced + e
            b_mod_q = mod_polynomial(b, modulus)
            b_polynomials.append(b_mod_q)
            labels.append(1)  # RLWE case
        else:
            # Case 2: Random b_i(x)
            random_b = random_polynomial(degree, modulus)
            b_polynomials.append(random_b)
            labels.append(0)  # This is random case
    
    return a_polynomials, b_polynomials, s, labels
# Example usage
num_polynomials = 2000 # Number of a_i(x), b_i(x) pairs
degree = n  # Degree of polynomials

# Generate RLWE Decision data
a_polys, b_polys, secret_poly, labels = generate_rlwe_decision_data(num_polynomials, degree, q, b_bound)

# Display the generated data
with open ("S2G\Crypto\LULbashevsky\\train.csv","w") as fil:
    labelX = [f"x_{i}, " for i in range(n)]
    fil.write(f"{''.join(labelX)}target\n")
    for i, (a, b, label) in enumerate(zip(a_polys, b_polys, labels)):
        b = (b.coef.tolist())
        fil.write(f"{', '.join(str(int(x)) for x in b)}, {label}\n")
        