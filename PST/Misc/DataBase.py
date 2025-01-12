import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('PST\Misc\databasefiles\inventory.db')
cursor = conn.cursor()

# Enable WAL mode
cursor.execute('PRAGMA journal_mode=WAL;')

# Get the list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
lis = []
lim = []
lin = []
# Iterate through each table
for table_info in tables:
    table_name = table_info[0]

    # Assuming your table has columns 'size' and 'igft' (replace with actual names)
    cursor.execute(f'SELECT * FROM {table_name};')
    rows = cursor.fetchall()
    
    # Find the index equivalent to 'size' and 'Small' in the specified line
for i, row in enumerate(rows):
    if 'Small' in row[1]:
        if 'Jade' in row[1]:
            lis.append(row[1] + ' ' + str(row[2]))  # Append index 2 to index 1
    elif 'Medium' in row[1]:
        if 'Jade' in row[1]:
            lim.append(row[1] + ' ' + str(row[2]))  # Append index 2 to index 1
    elif 'Nano' in row[1]:
        if 'Jade' in row[1]:
            lin.append(row[0]+ ' ' + row[1] + ' ' + str(row[2]))  # Append index 2 to index 1

with open ("PST\Misc\data.txt","w") as file:
    file.write("\n".join(lis))
    file.write('\n')
    file.write('------------')
    file.write('\n')
    file.write("\n".join(lim))    
    file.write('\n')
    file.write('------------')
    file.write('\n') 
    file.write("\n".join(lin))  
conn.close()


with open ("PST\Misc\data.txt","r") as file:

    lines = file.readlines()


li = []
for line in lines:
    # Split the line on spaces and combine the rest into a string
    words = line.split(' ')
    if len(words) > 2:
        rest_of_string = ' '.join(words[2:])
        li.append(rest_of_string.strip())
        print(rest_of_string)
    else:
        print("Not enough words in line:", line)
print(set(li))
print(len(set(li)))