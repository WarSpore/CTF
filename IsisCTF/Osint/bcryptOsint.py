import bcrypt
import itertools

# List of words
word_list = [
    "Mimosas", "Mimosa",'Italy',"Amsterdam", "Brunch", "Mom", "Love", "Birthday", "Trip", "Milan", "Starbucks", "Berlin",
    'Swarovski' ,'Swans','Tiramisu'
    , "Portofino",'Travel','Family','Vacation','In','Always','Remember','Destination'
]

word_list = ['I','Love','Portofino','Like','Always','Remember','Best','Destiniation','For','Ever','Is','Best','Travel','With','Mom','Very','Important','In',
             'Italy', "in", "Mimosa", "Mimosas", "Travel", "with","Tiramisu"]

# Numbers to be added at the end for different date formats
date_numbers = ["040865", "04081965",'4865','481965','0481965']

def generate_password_combinations(word_list, date_numbers):
    # Generate all possible 3-word combinations
    combinations_without_numbers = list(itertools.product(word_list, repeat=3))

    # Add date numbers at the end for each combination
    combinations_with_numbers = [(word1, word2, word3 + number) for word1, word2, word3 in combinations_without_numbers for number in date_numbers]

    return combinations_with_numbers

def runable():
    # Generate a salt with 10 rounds
    #salt = b'$2b$04$DkQOnBXHNLw2cnsmSEdM0u'  # Adjust the cost factor as needed

    # Hash a password using the generated salt
    password_combinations = generate_password_combinations(word_list, date_numbers)

    for password_tuple in password_combinations:
        password = ''.join(password_tuple).encode('utf-8')

        # Compare the hashed password with the given hash
        match = bcrypt.checkpw(password, b'$2b$04$DkQOnBXHNLw2cnsmSEdM0uyN3NHLUb9I5IIUF3akpLwoy7dlhgyEC')
        if match:
            print(f"Password Match: {match}")
            print(f"{password}")
            break

# Run the function
runable()
print("Done")
