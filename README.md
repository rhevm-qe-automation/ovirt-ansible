[![Build Status][travisimg]][travis]

# ovirt-ansible

Ansible roles for oVirt deployment.

Roles in this repository can configure nodes used as oVirt deployment members.

## Host groups

Each role has documentation, where you can find ``Target systems`` section.
This section specifies what kind of node you can apply relevant role.

### engine

This host group is meant for node where the oVirt Engine management is supposed
to be deployed.

### hypervisors

This host groups are meant for all nodes which are supposed to be used as
hypervisors of oVirt Engine.

Note that none of the roles in this repository adds these machines into
oVirt Engine.

### database

This host group is meant for node on which the database is supposed to be
deployed.

### dwh

This host group is meant for node on which the DWH is supposed to be deployed.

## Implemented roles

* [ovirt-collect-logs]
* [ovirt-common]
* [ovirt-engine-backup]
* [ovirt-engine-config]
* [ovirt-engine-install-packages]
* [ovirt-engine-remote-db]
* [ovirt-engine-setup]

## Example

Minimal playbook example

```yaml
---
- hosts: engine
  roles:
    - role: ovirt-common
    - role: ovirt-engine-install-packages
    - role: ovirt-engine-setup

- hosts: hypervisors
  roles:
    - role: ovirt-common
```

Minimal inventory example

```ini
[all:vars]
ovirt_engine_type=ovirt-engine
ovirt_engine_version=4.1
# Make sure that link to release rpm is working!!!
ovirt_rpm_repo: "http://resources.ovirt.org/pub/yum-repo/ovirt-release-master.rpm"
ovirt_engine_organization=of.ovirt.engine.com
ovirt_engine_admin_password=secret

[engine]
fqdn.of.ovirt.engine.com

[hypervisors]
fqdn.of.ovirt.hypervisor1.com
fqdn.of.ovirt.hypervisor2.com
```


[travisimg]: https://travis-ci.org/rhevm-qe-automation/ovirt-ansible.svg?branch=master
[travis]: https://travis-ci.org/rhevm-qe-automation/ovirt-ansible
[ovirt-collect-logs]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-collect-logs/README.md
[ovirt-common]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-common/README.md
[ovirt-engine-backup]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-engine-backup/README.md
[ovirt-engine-config]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-engine-config/README.md
[ovirt-engine-install-packages]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-engine-install-packages/README.md
[ovirt-engine-remote-db]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-engine-remote-db/README.md
[ovirt-engine-setup]: https://github.com/rhevm-qe-automation/ovirt-ansible/blob/master/roles/ovirt-engine-setup/README.md
