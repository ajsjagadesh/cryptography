from cryptography.fernet import Fernet

"""def gen_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as f:
        f.write(key)
    return key"""


def file_encrypt():
    with open ("key.key","rb") as kkey:
        key = kkey.read()
    fname = input("Enter file name to encrypt :")
    with open (fname,"rb") as data:
        string = data.read()
    en =Fernet(key)
    enc_data = en.encrypt(string)
    with open (fname,"wb") as data:
        data.write(enc_data)
    print("Encryption completed "+fname)

file_encrypt()


"""
key = gen_key()
en = Fernet(key)
data="hello how are you..!".encode()
encrypted_data = en.encrypt(data)
print(encrypted_data)"""
