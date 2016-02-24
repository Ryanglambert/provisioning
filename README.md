this script needs to be made more professional, but that doesn't mean it can't help you now!


Assumptions made by this script: 

- you have a `id_rsa.pub` in your .ssh folder
- you have the ip of the server
- the root password of the server

How to run it

- `git clone https://github.com/Ryanglambert/provisioning.git`
- `cd provisioning`
- `fab -H root@<serverip> -I -k`
    - Type in the root password for the server
- `ssh <youruserid>@serverip`

- YAHTZEE!

:)
