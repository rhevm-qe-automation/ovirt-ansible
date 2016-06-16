# rhevm-ansible
Ansible playbooks for ovirt management

    create playbook based on roles and deploy whatever you want

You must fill file 'hosts'
add a host for engine

        [engine]
        IP or FQDN

second, fill Install_engine.yml file
README for this file can be found in role engine-install readme

command for run playbook: 

        ansible-playbook -i hosts install_engine.yml

