oVirt Engine Local DB to Remote
===============================

- dump engine/dwh database on engine
- create databases/users on remote server and import dump files, install postgres if neccessary
- set engine from local db to remote

Target systems
--------------

* engine
* database

Requirements
------------

Preinstalled engine with local DB.
Preinstalled clean el7/linux based operating system on remote server.

Role Variables
--------------

```yaml
---
ovirt_engine_to_remote_db: [True, False] Change from local to remote engine database (default: True)
ovirt_engine_dwh_to_remote_db: [True, False] Change from local to remote DWH database (default: False)
```

Dependencies
------------

Role ovirt-engine-db-dump
Role ovirt-engine-remote-db

Example Playbook
----------------

```yaml
---
# in inventory file engine has ovirt_type=engine, database has ovirt_type=remote_db
- hosts: engine database
  vars:
    ovirt_engine_dwh_to_remote_db: True
  roles:
    - ovirt-engine-local-to-remote-db
```

Author Information
------------------

Lucie Leistnerova
lucie.leistnerova@gmail.com
