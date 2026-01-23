from Crypto.Util.number import getRandomRange, getRandomNBitInteger
import ast
from itertools import chain
import random

def zero_encoding(bitstring):
    """
    Return the 0-encoding of a binary string.
    Each encoding takes prefix up to i-1 and appends '1',
    if bit i == '0'.
    """
    encodings = []
    for i in range(len(bitstring)):
        if bitstring[i] == '0':
            prefix = bitstring[:i]
            encodings.append(prefix + '1')
    return encodings

def generate_encrypted_table(y, g, p, number, n_bits=32):
    table = []
    bitstring = bin(number)[2:].zfill(n_bits)

    for element in bitstring:
        encrypted_entry = []
        
        if element == "0":
            k = getRandomRange(1, p)
            a1 = pow(g,k,p)
            b1 = 1*pow(y,k,p)%p
            
            k = getRandomRange(1, p)
            a2 = pow(g,k,p)
            r = getRandomRange(1,p)
            b2 = r*pow(y,k,p)%p
    
            encrypted_entry.append((a1,b1))
            encrypted_entry.append((a2,b2))

        if element == "1":
            k = getRandomRange(1, p)
            a1 = pow(g,k,p)
            b1 = 1*pow(y,k,p)%p
            
            k = getRandomRange(1, p)
            a2 = pow(g,k,p)
            r = getRandomRange(1,p)
            b2 = r*pow(y,k,p)%p
            
            encrypted_entry.append((a2,b2))
            encrypted_entry.append((a1,b1))
        
        table.append(encrypted_entry)
    
    return table

# Set up challenge values
p = 1552518092300708935130918131258481755631334049434514313202351196288509170691316593175367469551763119843371637221007210577919
g = 2
x = getRandomRange(1, p)
number_to_guess = getRandomNBitInteger(32)
y = pow(g, x, p)
encrypted_table = generate_encrypted_table(y, g, p, number_to_guess)
cts = []

print("Welcome fellow rich person!")
print("Lets compare our bank accounts. I will tell you who's riches, me or you xD")
print("But lets be civilised, I will not give you the amount directly..")

same_counter = 0

while True:
    print("Menu:")
    print("1) Get parameters")
    print("2) Show encryption table")
    print("3) Encrypt your value. I promise I will not look at it :D")
    print("4) Submit encrypted values")
    print("5) Guess my secret number")
    print("6) Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        print(f"\np = {p}")
        print(f"g = {g}")
        print(f"y = {y}\n")

    elif choice == "2":
        print("\nEncrypted table (one row per bit):")
        print(encrypted_table)
        print()

    elif choice == "3":
        try:
            user_value = int(input("Amount in your bankaccount (No more than 32 bits): "))
            if user_value > 4294967295:
                print("Number must be less than 32 bits!")
                break
            userbitstring = bin(user_value)[2:].zfill(32)
            user_0encoded = zero_encoding(userbitstring)
        except:
            print("Must be a number!")
            continue

        user_cts = []

        for bitelement in user_0encoded:
            ct = [1, 1]
            for idx, bit in enumerate(bitelement):
                a, b = encrypted_table[idx][int(bit)]
                ct[0] = (ct[0] * a) % p
                ct[1] = (ct[1] * b) % p
            user_cts.append(tuple(ct))


        while len(user_cts) < len(encrypted_table):
            k = getRandomRange(1, p)
            a = pow(g, k, p)
            r = getRandomRange(1, p)
            b = (r * pow(y, k, p)) % p
            user_cts.append((a, b))

        random.shuffle(user_cts)
        print("Here is your ciphertext list (shuffled):")
        print(user_cts)
        print()

    elif choice == "4":
        if len(cts) > len(encrypted_table):
            print("Too many ciphertexts has been submitted!")
            exit(0)
        print("Submit your ciphertexts!")
        while len(cts) < len(encrypted_table):
            richer = False

            try:
                raw = input("Return [(a1,b1),(a2,b2),…] or ENTER to stop: ").strip()
                if not raw:
                    break
                ct = ast.literal_eval(raw)
            except Exception as e:
                print(f"Wrong format, try again. {e}")
                continue

            cts.extend(ct)

            for a, b in ct:
                if (a,b) in list(chain.from_iterable(encrypted_table)):
                    same_counter += 1
                if same_counter >= 2:
                    print("Bro why are you just sending the table back?")
                    exit(0)
                shared = pow(a, x, p)
                inv    = pow(shared, -1, p)
                if (b * inv) % p == 1:
                    richer = True
                    print("Haha I'm richer than you")
                    break
            if not richer:
                print("Damn you're richer than me. I wonder how much you really have?")

    elif choice == "5":
        try:
            guess = int(input("\nGuess my 32-bit secret number: ").strip())
            if guess == number_to_guess:
                print("\n🎉 How did you know???")
                print("flag{REDACTED}")
                break
            else:
                print("\n❌ Wrong!")
                break
        except ValueError:
            print("\n🚫 That wasn’t a valid integer.")

    elif choice == "6":
        print("\nGoodbye.")
        break

    else:
        print("\nInvalid option, try again.")
