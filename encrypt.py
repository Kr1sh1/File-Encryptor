import os
import hashlib
import sys
import base64

from cryptography.fernet import Fernet

class Cryptor:
    def __init__(self, password):
        self.__password = password

    def operate(self, file_):
        if file_.endswith("enc"):
            self.decrypt(file_)
        else:
            self.encrypt(file_)

    def decrypt(self, file_):
        file_name = "".join(file_.split(".")[:-1])

        with open(file_, "rb") as file_:
            save1 = file_.readline()
            save2 = file_.readline()
            save3 = file_.readline()
            salt = save3
            key = base64.urlsafe_b64encode(hashlib.pbkdf2_hmac("sha256", bytes(self.__password, encoding="utf-8"), salt, 100000, dklen=32))
            f = Fernet(key)
            decrypted = f.decrypt(save1)
            file_extention = f.decrypt(save2)
            save = decrypted

        with open(file_name + file_extention.decode(encoding="utf-8"), "wb") as file_:
            file_.write(save)

        os.remove(file_name + ".enc")

    def encrypt(self, file_):
        salt = os.urandom(64)
        key = base64.urlsafe_b64encode(hashlib.pbkdf2_hmac("sha256", bytes(self.__password, encoding="utf-8"), salt, 100000, dklen=32))
        f = Fernet(key)

        file_name = "".join(file_.split(".")[:-1])
        file_extention = "." + file_.split(".")[-1]

        with open(file_, "rb") as file_:
            file__ = file_.read()
            encrypted = f.encrypt(bytes(file__))
            save1 = encrypted
            save2 = f.encrypt(bytes(file_extention, encoding="utf-8"))
            save3 = salt
        
        with open(file_name + ".enc", "wb") as file_:
            file_.write(save1)
            file_.write(b"\n")
            file_.write(save2)
            file_.write(b"\n")
            file_.write(save3)

        os.remove(file_name + file_extention)

def main():
    password = sys.argv[1]
    files = sys.argv[2:]
    crypt = Cryptor(password)

    for file_ in files:
        crypt.operate(file_)

if __name__ == "__main__":
    main()
