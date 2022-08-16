# Declaring run
#!/bin/bash

# Get the IP address and subnet of the computer
ip = $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')
subnet = $(echo $ip | cut -d '.' -f 1-3)

# Get the file to run
file = Replica.py # This should be replaced with Replica.exe or whatever

# Run the file on all computers in the subnet
for i in {1..254}; do
    sshpass -p "password" ssh -o StrictHostKeyChecking=no user@$subnet.$i "bash -s" &lt; $file
done