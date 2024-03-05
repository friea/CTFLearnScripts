def xor_decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        decrypted += chr(ord(char) ^ key)
    return decrypted

def brute_force_xor(ciphertext):
    for key in range(256):
        decrypted_text = xor_decrypt(ciphertext, key)
        print(f"Key: {key}, Decrypted Text: {decrypted_text}")

ciphertext = "q{vpln'bH_varHuebcrqxetrHOXEj"
ciphertext_bytes = [ord(char) for char in ciphertext]

for key in range(256):
    decrypted_bytes = [byte ^ key for byte in ciphertext_bytes]
    decrypted_text = ''.join(chr(byte) for byte in decrypted_bytes)
    print(f"Key: {key}, Decrypted Text: {decrypted_text}")
