# import sha256
from hashlib import sha256
# text to hash
text = input("Enter the text to hash:")
hash_result = sha256(text.encode())

# print result
print("Hash:", hash_result.hexdigest())

