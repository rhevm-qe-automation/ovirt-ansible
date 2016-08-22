[![Build Status][travisimg]][travis]

# ovirt-ansible
Ansible playbooks for ovirt management

    create playbook based on roles and deploy whatever you want


## Requirements

Package sshpass installed for authentication

You must fill file 'hosts'
add a host for engine

        [engine]
        IP or FQDN

second, fill Install_engine.yml file
README for this file can be found in role engine-install readme


command for run playbook:

        ansible-playbook -i example/inventory/install_engine.inv example/playbooks/install_engine.yml

## Implemented roles

* [ovirt-collect-logs]
* [ovirt-common]
* [ovirt-engine-backup]
* [ovirt-engine-dwh-remote]
* [ovirt-engine-install-packages]
* [ovirt-engine-remote-db]
* [ovirt-engine-setup]


[travisimg]: https://travis-ci.org/StLuke/ovirt-ansible.svg?branch=master
[travis]: https://travis-ci.org/StLuke/ovirt-ansible
[ovirt-collect-logs]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-collect-logs/README.md
[ovirt-common]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-common/README.md
[ovirt-engine-backup]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-engine-backup/README.md
[ovirt-engine-dwh-remote]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-engine-dwh-remote/README.md
[ovirt-engine-install-packages]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-engine-install-packages/README.md
[ovirt-engine-remote-db]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-engine-remote-db/README.md
[ovirt-engine-setup]: https://github.com/StLuke/ovirt-ansible/blob/master/roles/ovirt-engine-setup/README.md
