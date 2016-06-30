[![Build Status][travisimg]][travis]

# ovirt-ansible
Ansible playbooks for ovirt management

    create playbook based on roles and deploy whatever you want


Requirements
------------

Package sshpass installed for authentication

You must fill file 'hosts'
add a host for engine

        [engine]
        IP or FQDN

second, fill Install_engine.yml file
README for this file can be found in role engine-install readme


command for run playbook:

        ansible-playbook -i example/inventory/install_engine.inv example/playbooks/install_engine.yml

[travisimg]: https://travis-ci.org/StLuke/ovirt-ansible.svg?branch=master
[travis]: https://travis-ci.org/StLuke/ovirt-ansible
