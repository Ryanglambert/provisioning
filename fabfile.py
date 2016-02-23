import os.path
from fabric.api import run, sudo, env, execute, settings
from fabric.operations import run, put

user = raw_input('what your username will be on server: ')


def create_user():
    sudo('adduser {user} --gecos \'no, no, no, no, no\' --disabled-password'.format(user=user))
    sudo('echo \"{user}:metis\" | sudo chpasswd'.format(user=user))
    sudo('echo \"{user}  ALL=(ALL:ALL) ALL\" >> /etc/sudoers'.format(user=user))

def copy_ssh_key():
    keyfile = '/tmp/id_rsa.pub'
    sudo('mkdir -p /home/{user}/.ssh && chmod 700 /home/{user}/.ssh && chown {user}:{user} /home/{user}/.ssh'.format(user=user))
    put('~/.ssh/id_rsa.pub', keyfile)
    sudo('touch /home/{user}/.ssh/authorized_keys'.format(user=user))
    sudo('cat %s >> /home/{user}/.ssh/authorized_keys'.format(user=user) % keyfile)
    sudo('chown {user}:{user} /home/{user}/.ssh/authorized_keys'.format(user=user))
    sudo('rm %s' % keyfile)


def run_provision_script():
    # with settings(prompts={'Do you want to continue [Y/n]? ': 'Y'}):
    sudo('echo "y\n" | apt-get update')
    sudo('apt-get install python-pip python-dev build-essential')
    sudo('pip install --upgrade pip')

# def set_user_perms():
#     sudo('echo

user_home = os.path.expanduser('~')
ssh_loc = os.path.join(user_home, '.ssh/id_rsa.pub')

if os.path.isfile(ssh_loc) == True:
    execute(create_user)
    print("COPYING SSH KEY TO USER " + str(['####'] * 3))
    execute(copy_ssh_key)
    print("RUN PROVISION BASH SCRIPT" + str(['####'] * 3))
    
    execute(run_provision_script)

else:
    print "you don't have an id_rsa.pub go make one and put it in your .ssh folder"
