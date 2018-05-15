oVirt Engine Cleanup
====================

This role generates answerfile for engine-cleanup and execute it.

Requirements
------------

oVirt installed.

Role Variables
--------------

```yaml
---
ovirt_engine_version: one of ["3.6", "4.0", "4.1"..]    
ovirt_engine_db_host: IP or hostname of PostgreSQL server for engine database (default: 'localhost')
ovirt_engine_db_port: Server listening port (default 5432)
ovirt_engine_db_name: DB name for ovirt-engine (default: 'engine')
ovirt_engine_db_user: DB user which can access ovirt-engine DB (default: 'engine')
ovirt_engine_db_password: password for user of ovirt-engine DB
ovirt_engine_dwh_db_host: IP or hostname of PostgreSQL server for DWH database (default: 'localhost')
ovirt_engine_dwh_db_port: Server listening port (default 5432)
ovirt_engine_dwh_db_name: DB name for ovirt-engine-dwh (default: 'ovirt_engine_history')
ovirt_engine_dwh_db_user: DB user which can access ovirt-engine-dwh DB (default: 'ovirt_engine_history')
ovirt_engine_dwh_db_password: password for user of ovirt-engine DB
```

Dependencies
------------

* [oVirt.engine-setup](https://galaxy.ansible.com/oVirt/engine-setup/)

Example Playbook
----------------

```yaml
---
- hosts: engine
  remote_user: root
  vars:
    ovirt_engine_version: 4.0
    ovirt_engine_db_host: 'localhost'
    ovirt_engine_db_port: 5432
    ovirt_engine_db_name: 'engine'
    ovirt_engine_db_user: 'engine'
    ovirt_engine_db_password: 'password'
    ovirt_engine_dwh_db_host: 'localhost'
    ovirt_engine_dwh_db_port: 5432
    ovirt_engine_dwh_db_name: 'ovirt_engine_history'
    ovirt_engine_dwh_db_user: 'ovirt_engine_history'
    ovirt_engine_dwh_db_password: 'password'      
  roles:
    - { role: ovirt-engine-cleanup }
```

License
-------

GPLv3

Author Information
------------------

Lukas Bednar
lbednar@redhat.com
