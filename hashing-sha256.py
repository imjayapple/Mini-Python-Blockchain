# import sha256
from hashlib import sha256

# text to hash
text = input("Enter the text to hash:")
hash_result = sha256(text.encode())

# print result
print("Hash:", hash_result.hexdigest())

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    hash_object = sha256()

    try:
        with open(file_path, 'rb') as file:
            # Read the file in chunks for memory efficiency
            for chunk in iter(lambda: file.read(4096), b''):
                hash_object.update(chunk)

        return hash_object.hexdigest()

    except FileNotFoundError:
        print("File not found.")

# Prompt the user for the file path
file_path = input("Enter the file path: ")

# Calculate the hash of the file
file_hash = calculate_file_hash(file_path)

# Calculate the has of the input file
calculated_hash = calculate_file_hash(text)

text = input("Enter the text to hash: ")

# Prompt the user for the expected hash
expected_hash = input("Enter the expected hash: ")

# Verify the hash
if calculated_hash == expected_hash:
    print("Hash verification passed.")
else:
    print("Hash verification failed.")