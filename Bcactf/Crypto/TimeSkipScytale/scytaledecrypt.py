def scytale_decrypt(ciphertext, columns, rows):
    grid = [[''] * columns for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(columns):
            if index < len(ciphertext):
                grid[r][c] = ciphertext[index]
            else:
                grid[r][c] = '_'
            index += 1
    plaintext = ''.join([''.join(row[c] for row in grid) for c in range(columns)])
    return plaintext

def try_all_combinations(ciphertext):
    length = len(ciphertext)
    results = []
    
    for columns in range(1, 50 + 1):
        for rows in range(1, 50 + 1):
            if columns * rows >= length:
                plaintext = scytale_decrypt(ciphertext, columns, rows)
                results.append((columns, rows, plaintext))
    
    return results

ciphertext = "hsggna0stiaeaetteyc4ehvdatyporwtyseefregrstaf_etposruouoy{qnirroiybrbs5edmothssavetc8hebhwuibihh72eyaoepmlvoet9lobulpkyenf4xpulsloinmelllisyassnousa31mebneedtctg_}eeedeboghbihpatesyyfolus1lnhnooeliotb5ebidfueonnactayseyl"

results = try_all_combinations(ciphertext)
with open ("Bcactf\\Crypto\\TimeSkipScytale\\result.txt","w") as fil:
    for columns, rows, plaintext in results:
        fil.write(f"Columns: {columns}, Rows: {rows}")
        fil.write(f"Plaintext: {plaintext}\n")
    
