from cryptography.fernet import Fernet

def decrypt():
    fname = input("Enter file name to decrypt :")
    with open (fname,"rb") as edata:
        string = edata.read()
    with open ("key.key","rb") as k:
        key = k.read()
    dc = Fernet(key)
    d_data = dc.decrypt(string)
    with open (fname,"wb") as data:
        data.write(d_data)

decrypt()
