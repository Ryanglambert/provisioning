# What it does
- Upgrades aptitude (apt-get)
- Installs python-pip python-dev build-essential
- Adds user and ssh key

# Assumptions made by this script: 

- you have a `id_rsa.pub` in your .ssh folder
- you have the ip of the server
- the root password of the server

# How to run it

- `git clone https://github.com/Ryanglambert/provisioning.git`
- `cd provisioning`
- `fab -H root@<serverip> -I -k`
    - Give it the username you will use on the server
    - Type in the root password for the server
    - at some point it will ask you to type yes (working on removing this)
- `ssh <youruserid>@serverip`

# YAHTZEE!

:)
