# Installation des outils pour debuguer linux

Dépendances :
Alors en fait rien sur galaxy, mais pour pip, il y en a une sur importante, c'est passlib pour les mots de passe. Ne pas oublier de faire "pip install -r requirements.txt".

~~~bash
source ~/venv/bin/activate
cd ~/Documents/ansible-role-develop
pip install -r requirements.txt
molecule[docker,lint]
~~~

~~~bash
molecule --version
molecule drivers
[[ -d ~/.ansible/roles/mpatron.ansible_role_develop ]] && echo "Le lien existe déjà" || ln -s ~/Documents/ansible-role-develop ~/.ansible/roles/mpatron.ansible_role_develop
cd ~/Documents/ansible-role-develop
molecule test
podman run -it docker.io/almalinux:9 /bin/bash
podman run -it docker.io/ubuntu:24.04 /bin/bash
apt update && apt install -yqq vim curl dnsutils nmap tcpdump lsof iotop htop sysstat wget iptraf
# iostat & iotop  => performance disques
# iptraf =>  performance reseau
~~~

~~~bash
podman run -it --rm \
 --cap-add=SYS_ADMIN \
 --cap-add=SYS_RESOURCE \
 --device "/dev/fuse" \
 --hostname=ansible-dev-container \
 --name=ansible-dev-container \
 --security-opt "apparmor=unconfined" \
 --security-opt "label=disable" \
 --security-opt "seccomp=unconfined" \
 --user=root \
 --userns=host \
 -e SSH_AUTH_SOCK=$SSH_AUTH_SOCK \
 -v $HOME/.gitconfig:/root/.gitconfig \
 -v $PWD:/workdir \
 -v $SSH_AUTH_SOCK:$SSH_AUTH_SOCK \
 ghcr.io/ansible/community-ansible-dev-tools:latest
~~~

~~~bash
molecule test --scenario-name runinpodman
clear && molecule test --scenario-name runinpodman --report --command-borders

molecule create --scenario-name runinpodman
podman ps
molecule login --scenario-name runinpodman

molecule destroy --scenario-name runinpodman
molecule converge --scenario-name runinpodman
~~~

~~~txt
https://github.com/ansible/molecule/blob/main/docs/examples/podman.md
https://github.com/ansible/molecule/blob/main/tests/fixtures/integration/test_command/molecule/podman/molecule.yml
~~~
