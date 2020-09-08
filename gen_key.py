from cryptography.fernet import Fernet

def gen_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as f:
        f.write(key)
    print("key generated and saved")

gen_key()

