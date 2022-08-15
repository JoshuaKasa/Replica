from Extensions import get_extensions
from cryptography.fernet import Fernet
from os import walk
from os import path

# Getting key
key = "Insert your decryption key here: "
f = Fernet(key)

# Extensions
extensions = get_extensions()

# Scanning entire C drive
for root, dirs, files in walk("C:\\"):
    # Grabbing files
    for file in files:
        fpath  = "{0}\\{1}".format(root, file)
        ext = path.splitext("{0}\\{1}".format(root, file))[1]

        # Decrypting only files with specific extension
        if ext in extensions:
            with open(fpath, "rb") as of:
                encrypted: bytes = of.read()

            decrypted = f.decrypt(encrypted)

            with open(fpath, "wb") as of:
                of.write(decrypted)