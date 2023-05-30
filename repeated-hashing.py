from hashlib import sha256

# Function to calculate the hash of a text
def calculate_text_hash(text):
    hash_object = sha256()
    hash_object.update(text.encode())
    return hash_object.hexdigest()

# Prompt the user for input
text = input("Enter the text to hash: ")

# Prompt the user for the number of iterations
num_iterations = int(input("Enter the number of iterations for the hash chain: "))

# Initialize the current text as the original input
current_text = text
