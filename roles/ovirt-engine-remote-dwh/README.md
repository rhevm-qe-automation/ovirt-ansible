oVirt Engine Remote DWH setup
=============================

Sets up a remote DWH service for your ovirt-engine installation.

Target systems
--------------

* engine

Requirements
------------

Preinstalled clean environment with configured repositories.

Dependencies
------------

* [oVirt.repositories](https://galaxy.ansible.com/oVirt/repositories/)
* [oVirt.engine-setup](https://galaxy.ansible.com/oVirt/engine-setup/)

Assumptions
-----------

- Both the hosts where engine and the DWH is to be setup should have valid FQDN's resolvable internally
- Ports 80, 443, 5432 should be open on both these hosts.
- root password login(for now) has to be enabled for DWH host to configure itself with that host


Example Playbook
----------------

First would be the installation of the Engine machine.
For this you can use the following roles:
 - [oVirt.engine-setup](https://galaxy.ansible.com/oVirt/engine-setup)
 - [oVirt.repositories](https://galaxy.ansible.com/oVirt/repositories)

```yaml
---
- hosts: engine
  roles:
    - role: oVirt.repositories
      ovirt_repositories_ovirt_release_rpm: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release41.rpm'
    - role: oVirt.engine-setup
      ovirt_engine_setup_type: "ovirt-engine"
      ovirt_engine_setup_hostname: "localhost"
      ovirt_engine_setup_version: "4.1"
      ovirt_engine_setup_organization: "example.com"
      ovirt_engine_setup_dwh_db_configure: false
      ovirt_engine_setup_dwh_db_host: "remotedwh.ovirt.org"
      ovirt_engine_setup_firewall_manager: null
```


After that you have to configure your remote DWH installation to the previous host which has the ovirt-engine installation which again has two possibilities

### Possibility #1: The database of dwh is on dwh machine

```yaml
---
- hosts: dwh-remote
  tasks::
    - include_role:
        name: oVirt.repositories
        vars:
          ovirt_repositories_ovirt_release_rpm: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release41.rpm'
    - name: Install ovirt-engine-dwh-setup package
      package:
        name: ovirt-engine-dwh-setup
        state: present
    - include_role:
        name: ovirt-engine-remote-dwh
        vars:
          ovirt_engine_type: 'ovirt-engine'
          ovirt_engine_version: '4.1'
          ovirt_engine_host_root_passwd: 'admin123' # the root password of the host where ovirt-engine is installed
          ovirt_engine_firewall_manager: 'firewalld'
          ovirt_engine_db_host: 'dwhmanualenginetest.ovirt.org' # FQDN of the ovirt-engine installation host, should be resolvable from the new DWH host
          ovirt_engine_host_fqdn: 'dwhmanualenginetest.ovirt.org'
          ovirt_engine_dwh_db_host: 'localhost'
          ovirt_engine_history_db_on_dwhservice_host: True ovirt-engine-remote-dwh
```

After this you have to restart your ovirt-engine on the host installed by doing a `service ovirt-engine restart`

### Possibility #2: The database of dwh on 3rd machine

This approach will follow a 3 box VM setup.

For clarity sake, the VM's can be assumed for now as

- VM A: `engine.ovirt.org`: which stored `engine` db and the main engine installation.
- VM B: `dwhservice.ovirt.org`: which will host the dwh service
- VM C: `dwhdb.ovirt.org`: which will store the `ovirt_engine_history` db


##### On VM C

the VM has to be setup for the `ovirt_engine_history` VM which is to be used by `dwhservice.ovirt.org` VM.

```yaml
---
- hosts: dwhdb
  vars:
    # a value of '139.162.45.0/24' would take for 'engine_vm_network_cidr' when the IP
    # address of the engine VM is '139.162.45.249'. The value for the value below
    # is calculated similarly
    engine_vm_network_cidr: '1.2.3.4' # Network where the Engine VM lies
    dwhservice_vm_network_cidr: '1.2.3.5'
    ovirt_engine_dwh_db_password: 'password'
  roles:
    - role: ovirt-engine-remote-dwh/install-postgresql

```

##### On VM B

Now VM which hosts the `dwhservice` needs to be setup.

```yaml
---
- hosts: dwhservice
  tasks::
    - include_role:
        name: oVirt.repositories
        vars:
          ovirt_repositories_ovirt_release_rpm: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release41.rpm'
    - name: Install ovirt-engine-dwh-setup package
      package:
        name: ovirt-engine-dwh-setup
        state: present
    - include_role:
        name: ovirt-engine-remote-dwh
        vars:
          ovirt_engine_type: 'ovirt-engine'
          ovirt_engine_version: '4.1'
          ovirt_engine_host_root_passwd: 'password'  # the root password of the host where ovirt-engine is installed
          ovirt_engine_firewall_manager: 'firewalld'
          ovirt_engine_host_fqdn: 'testengine.ovirt.org'  # FQDN of the ovirt-engine installation host, should be resolvable from the new DWH host
          ovirt_engine_db_host: 'testengine.ovirt.org'
          ovirt_engine_dwh_db_host: 'testdwhdb.ovirt.org'
          ovirt_engine_dwh_db_password: 'password'
          ovirt_engine_history_db_on_dwhservice_host: False


```

Now restart `ovirt-engine` in VM A by doing a `systemctl restart ovirt-engine`

This will setup your ovirt-engine setup ready for the incoming remote DWH installation setup

Author Information
------------------

Tasdik Rahman
tasdik95@gmail.com
