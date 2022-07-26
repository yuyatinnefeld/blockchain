import hashlib

print("## ORIGINAL MESSAGE")
message="hi hey ho"
print(message, "\n")


print("## HASH FUNC: SHA256")
hash_func_1 = hashlib.sha256()
print(hash_func_1)
encoded_string = message.encode()
hash_func_1.update(encoded_string)
print("ENCRYPTED: ",hash_func_1.hexdigest(), "\n")
# print(crypt_1.digest_size)
# print(crypt_1.block_size)

print("## HASH FUNC: MD5")
hash_func_2 = hashlib.md5()
print(hash_func_2)
encoded_string = message.encode()
hash_func_2.update(encoded_string)
print("ENCRYPTED: ",hash_func_2.hexdigest(), "\n")

print("ALGORITHM VARIANTS: ")
print(hashlib.algorithms_available, "\n")


print("SAVE THE DATA")

import hashlib
 
def save_encoded_text(original, encoded):
    hash_sha1 = hashlib.sha1()
    with open(original, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    
    with open(encoded, 'w') as f:
        f.write(hash_sha1.hexdigest())        
 
# create a file
original_text = "message.txt"
encoded_text = "encoded.txt"
save_encoded_text("message.txt", "encoded.txt")
