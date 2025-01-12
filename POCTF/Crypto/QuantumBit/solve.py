import numpy as np

# Given data
Qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0,
          0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1,
          0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
          0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]

Bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 
         'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 
         'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 
         'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 
         'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 
         'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']

Measurements = [0, 1, None, 1, 0, None, 1, 1, None, 0, 1, None, 0, 1, None, 0, 
                1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 1, None, 1, 
                0, None, 0, 0, None, 0, 1, None, 0, 1, None, 1, 1, None, 1, 
                0, None, 1, 0, None, 0, 1, None, 0, 1, None, 0, 1, None, 1, 
                0, None, 1, 0, None, 0, 1, None, 0, 0, None, 0, 1, None, 1, 
                1, None, 1, 1]

# Process Measurements based on Qubits and Bases
for i in range(len(Qubits)):
    if Measurements[i] is None:  # If measurement is unknown
        if Bases[i] == 'R':
            Measurements[i] = Qubits[i]  # Directly take the qubit value
        elif Bases[i] == 'D':
            Measurements[i] = np.random.randint(2)  # Randomly measure in diagonal base (0 or 1)

# Given data
Encrypted_Message = [0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 
                     0x6a, 0x0b, 0x0c, 0x50, 0xd4, 0x5a, 0x71, 0x87, 
                     0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 
                     0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b]

# Decrypting the message
li = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1]

Decrypted_Message = []
for i in range(len(Encrypted_Message)):
    decrypted_byte = Encrypted_Message[i] ^ li[i]  # XOR the encrypted byte with the corresponding measurement
    Decrypted_Message.append(chr(decrypted_byte))

# Output decrypted message
print("".join(Decrypted_Message))