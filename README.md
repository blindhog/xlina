# xlina
Cisco ASA &amp; FTD Config Parsers and Organizers

# Files
- organize_acls.py - Extract and organize access-list configurations and organizes associated objects and object-groups.
- organize_anyconnect.py - Extract and organize Anyconnect profiles and associated group policies, auth servers, access-lists, etc
- organize_static_nats.py - Extract and organize static nat configurations and associated objects and object-groups
- organize_auto_nat.py - Extract and organize auto nat configurations with associated objects
- organize_crypto_maps.py - Extract and organize crypto map configurations and associated access-lists, transform-sets, tunnel-groups, etc
- xlina.py - xlina python class file. 


# Usage
## Install python requirements
python3 -m pip install -r requirements.txt

## Usage: organize_acls.py
python3 organize_acls.py [-h] -f [FILES [FILES ...]]

## Usage: organize_anyconnect.py 
python3 organize_anyconnect.py [-h] -f [FILES [FILES ...]]

## Usage: organize_static_nats.py
python3 organize_static_nats.py [-h] -f [FILES [FILES ...]]

## Usage: organize_auto_nat.py
python3 organize_auto_nat.py [-h] -f [FILES [FILES ...]]

## Usage: organize_crypto_maps.py
python3 organize_crypto_maps.py [-h] -f [FILES [FILES ...]]


# Tips:
Process more than one config file at a time<br>
python3 organize_script.py -f configs/ASA-config1.cfg /file/path/ASA-config2.cfg<br>
python3 organize_script.py -f configs/*<br>
python3 organize_script.py -f configs/*.cfg<br>
<br>
Redirect output to a text file<br>
python3 organize_script.py -f ASA-config1.cfg > ASA-config1-organized.txt<br>
<br>
Use the 'less' command to scroll through output<br>
python3 organize_script.py -f ASA-config1.cfg | less<br>
<br>






