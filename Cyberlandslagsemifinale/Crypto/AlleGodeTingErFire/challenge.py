
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes, isPrime
import sage



# Quaternion algebra over the rational numbers, i^2 = -1 and j^2 = -1
Q = QuaternionAlgebra(QQ, -1, -1)
p = getPrime(64)

assert len(FLAG) % 4 == 0

step = len(FLAG) // 4
flag_parts = [FLAG[i : i + step] for i in range(0, len(FLAG), step)]
flag_parts = [bytes_to_long(part) for part in flag_parts]

flag_quaternion = Q(flag_parts)
p_quaternion = Q(four_squares(QQ(p)))

x = flag_quaternion * p_quaternion

li = [509854650183320711588989587902344170658948806928491972305348081972245096/17852010398400078143 - 33905334237190827320667807445954378369551770685520584058719936013310291468/17852010398400078143 - 12671672548331161305476952667992846598499969939704088887753890054562122517113/17852010398400078143 - 1077109743592286455855412651400863895177143006998267516576715464197122168252988415/17852010398400078143]

for i in li:
    print(long_to_bytes(i))

with open("output.txt", "w") as fout:
    fout.write(f"{x = }\n")
