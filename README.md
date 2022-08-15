> :warning: **Warning:** this project just for run as test & learn ansible all important data(password,keys,..) hard coded dont use this in real word!

## **Crate multi servers:**
    - (in ubuntu can use multipass or VMs or...)
    - sudo multipass launch lts --name database
    - sudo multipass launch lts --name webserver
    - sudo multipass launch lts --name app
    - sudo multipass list

## **Bootstrap:**
- in every server for bootstrap can connect with password for first time:
    ` connect with: sudo multipass shell <name> `
        - sudo nano /etc/ssh/sshd_config
            PasswordAuthentication yes
            PermitEmptyPasswords yes
        - sudo systemctl restart sshd
- Tasks: 
    - update os
    - create a user
    - copy ssh public key
    -  copy sudoers file

- Run bootstrap (for first time connnect only)
    ` ansible-playbook --ask-become-pass --ask-pass -u root bootstrap.yml `

#### Run ansible playbook:
` ansible-playbook site.yml `

> client <------> loadbalancer <------> nginx(webserver) <------> app <------> DataBase
---
## **Servers**:
    - ALL:
        1. copy ssh public key from local
        2. copy ssh config file
        3. install docker

    - DataBase:
        1. install postgresql with docker

    - Load Balancer:
        1. install nginx and config as a loadbalancer

    - App Server
        1. copy project on server
        2. intall requirements
        3. install uwsgi (uwsgi as a Gateway Interface)
        4. install supervisor
        5. run wsgi as a service with supervisor on server
        6. install nginx
        7. config nginx as a webserver

---

## **Multiple envs**
    in inventories folder each folder as a environment (like: test,dev,stage,prod...)
    run : `ansible-playbook -i inventories/test/hosts site.yml` (test set as default in ansible.cfg)
    vars: in group_vars for each group (see all vars: ansible-inventory -i inventories/test --list)


## **deploy django app**
    "If you need to deploy a big number of apps on a single server, or a group of servers, the Emperor mode is just the ticket.
    It is a special uWSGI instance that will monitor specific events and will spawn/stop/reload instances (known as vassals, when managed by an Emperor) on demand"

        1. create a vassal dir (usually its /etc/uwsgi/vassals/)
        2. install supervisor & create a service with command ( uwsgi --empror vassals/ )
        3. create uwsgi config file (its create .sock file! give it to webserver)
        4. link uwsgi config file to vassals directory & touch this file