# Define the values of N and gamma

# Source used https://users.monash.edu.au/~rste/LSBSRSA.pdf

N = 12551950061305391361769682591853645824454142164006354660748594890465203674895994518975972435507528885623152014078638688067853389293128315013359788310452247166035470837105812135923054941452662044834505713253254770888250661478584019788790756907964004401928510668722946857249955152028909715903064862240436235107701280555816467693331539259548248190399412456941024971456489003117919421630536429645704890849913878972123057302656217796377748694180865542148630429486955684075038420318669037862998326777369014284557821474502575975035009047074384122773113772031583147904934771394681966331229494960038994375776809  # example value
alpha = 600  # example value
modulus = 2^alpha

def compute_s_candidates(N, alpha):
    # Step 1: Define modulus values for 2^alpha and 2^(2*alpha)
    modulus_alpha = 2 ** alpha
    modulus_2alpha = 2 ** (2 * alpha)
    
    # Step 2: Find candidates for l by solving x^2 ≡ N (mod 2^alpha)
    try:
        l_candidates = Mod(N, modulus_alpha).sqrt(all=True)
        print(f"Candidates for l (solutions to x^2 ≡ N mod 2^{alpha}): {l_candidates}")
    except ValueError:
        print("No solutions for x^2 ≡ N mod 2^alpha.")
        return []
    
    # Step 3: Compute s_H and s_0 for each l candidate
    s0_candidates = []
    for l in l_candidates:
        # Convert l to an integer modulo 2^(2*alpha)
        l = Integer(Mod(l, modulus_2alpha))
        
        # Compute l^2 and the value (N - l^2) mod 2^(2*alpha)
        l_square = (l * l) % modulus_2alpha
        N_minus_l_square = (N - l_square) % modulus_2alpha

        # Compute the multiplicative inverse of l modulo 2^(2*alpha)
        try:
            l_inverse = l.inverse_mod(modulus_2alpha)
        except ZeroDivisionError:
            print(f"Cannot compute inverse of l = {l} modulo 2^{2*alpha}. Skipping this l.")
            continue
        
        # Compute s_H = l^(-1) * (N - l^2) mod 2^(2*alpha)
        s_H = (l_inverse * N_minus_l_square) % modulus_2alpha
        
        # Compute s_0 = 2l + s_H mod 2^(2*alpha)
        s_0 = (2 * l + s_H) % modulus_2alpha
        s0_candidates.append(s_0)
        print(f"For l = {l}: s_H = {s_H}, s_0 = {s_0}")
    
    # Step 4: Generate candidates for s by toggling the top 2 bits of s_0
    s_candidates = []
    for s_0 in s0_candidates:
        for i in range(4):  # Toggle the top 2 bits (2^1 and 2^0)
            s = s_0 + (i << (2 * alpha - 2))  # Add the 2 MSB combinations
            s_candidates.append(s)
    
    return s_candidates

def factor_N_via_candidates(N, s_candidates):
    # Step 5: Try to solve x^2 - s * x + N = 0 for each candidate s
    for s in s_candidates:
        # Define the quadratic equation x^2 - s*x + N = 0
        x = var('x')
        equation = x^2 - s * x + N == 0
        
        # Solve the quadratic equation
        solutions = solve(equation, x)
        
        for sol in solutions:
            # Extract the right-hand side value for x and ensure it's an integer
            p_candidate = sol.rhs()
            if p_candidate.is_real():
                p_candidate = Integer(p_candidate)
            
            # Check if p_candidate is an integer factor of N
            if N % p_candidate == 0:
                q_candidate = N // p_candidate
                print(f"Factorization found: p = {p_candidate}, q = {q_candidate}")
                return p_candidate, q_candidate  # Return the factors
    
    print("No factors found with the given candidates.")
    return None, None


# Compute candidates for s_0 and s
s_candidates = compute_s_candidates(N, alpha)

# Attempt to factor N using the candidates
p, q = factor_N_via_candidates(N, s_candidates)
if p and q:
    print(f"Factors of N: p = {p}, q = {q}")
else:
    print("Failed to factor N.")





