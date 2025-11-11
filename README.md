on working...

Dépendances :
Alors en fait rien sur galaxy, mais pour pip, il y en a une sur importante, c'est passlib pour les mots de passe. Ne pas oublier de faire "pip install -r requirements.txt".

source ~/venv/bin/activate
cd ~/Documents/ansible-role-develop
pip install -r requirements.txt
molecule[docker,lint]

(venv) mickael@deborah:~/Documents/ansible-role-develop$ molecule --version
molecule 25.9.0 using python 3.14 
    ansible:2.20.0
    default:25.9.0 from molecule
(venv) mickael@deborah:~/Documents/ansible-role-develop$ molecule drivers
default

molecule drivers

source ~/venv/bin/activate
cd ~/Documents/ansible-role-develop
molecule test

podman run -it docker.io/almalinux:9 /bin/bash
podman run -it docker.io/ubuntu:24.04 /bin/bash

apt update && apt install -yqq vim curl dnsutils nmap tcpdump lsof iotop htop sysstat wget iptraf
# iostat & iotop  => performance disques
# iptraf =>  performance reseau
