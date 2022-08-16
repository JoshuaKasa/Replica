# **What is Replica?**

Replica is a simple but efficient undetectable ransomware written in Python for Windows.</br>
The main difference between Replica and other Ransomwares is the fact that Replica stores each of it's key in a database.</br>
Replica also runs on all computers connected to the same subnet.

``Warning! Replica is a project only for demonstration purposes, don't use it in any malicious way.``

# **Libraries used**
```
os -> For getting Windows files.
socket -> For getting host name.
mysql -> For connecting and sending informations to the database.
getpass -> For getting Desktop path.
fernet -> For encrypting files.
win32api -> For showing warning messages.
```

# **How does it work?**

Replica simply works by generating a key using the ``Fernet`` library and using that key for encrypting all of the files with a certain extension, you can check and modify the extenions in the ``Extensions.py`` file.

After generating the key, the program iterates through every file inside the ``C:`` drive, first it checks if the file extension is inside the possible extensions.</br>
If the extension is in the possible extensions, it tries to encrypt the file, if the file can't be modified (if it requires administrator priviligies) then it skips that file, else it gets encrypted.

After every file gets encrypted, a text file gets created in the ``Desktop``, inside the file there will be some text (you can check it and modify it from the main python file).</br>
The text file, should contain the steps to get the files back but most importantly it's ID (which is the host name).

``NOTE THAT REPLICA ALSO ENCRYPTS PY FILES, SO IT SHOULD BE RUNNED AS A .exe FILE``

# **How to decrypt?**
After money and proof have been sent, the victim should send it's ID and you can then give the victim it's key along with the decryption program (you can find the key inside the database).
