import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class CryptoClass:
    def __init__(self):
        self.base64_text = None
        self.cipher_data = None
        self.cipher_text = None
        self.iv_bytes = bytes([0] * 16)  # 16 bytes of 0s for initialization vector
        self.key = "This is the super secret key 123"
        self.plain_text = None

    def aes256_decrypt(self, cipher_data, key, iv_bytes):
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv_bytes)
        plain_text = unpad(cipher.decrypt(cipher_data), AES.block_size)
        return plain_text.decode()

    def aes256_encrypt(self, plain_text, key, iv_bytes):
        plain_text = pad(plain_text.encode(), AES.block_size)
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv_bytes)
        cipher_text = cipher.encrypt(plain_text)
        return base64.b64encode(cipher_text).decode()

    def aes_decrypted_string(self, base64_text):
        cipher_data = base64.b64decode(base64_text)
        self.plain_text = self.aes256_decrypt(cipher_data, self.key, self.iv_bytes)
        return self.plain_text

    def aes_encrypted_string(self, plain_text):
        self.plain_text = plain_text
        cipher_data = self.aes256_encrypt(plain_text, self.key, self.iv_bytes)
        self.cipher_text = base64.b64encode(cipher_data).decode()
        return self.cipher_text
    
crypto_class = CryptoClass()
encrypted_passwd = "u734blSGyPt7eobqiWxFOg==&#10;    "
encrypted_username = "amFjaw==&#13;&#10;    "

# Decrypt username
decrypted_username = crypto_class.aes_decrypted_string(encrypted_username)
print("Username: " + " "  + decrypted_username)

#Decrypt password
decrypted_passwd = crypto_class.aes256_decrypt(encrypted_passwd)
print("Password: " + " "  + decrypted_passwd)
