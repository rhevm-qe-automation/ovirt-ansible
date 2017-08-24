oVirt Engine dump
=================

- get DB variables (database, user, password, ...)
- get dump of engine and dwh database

Target systems
--------------

* engine

Requirements
------------

Preinstalled engine with local DB.

Role Variables
--------------

```yaml
---
ovirt_engine_db_dump_dwh: [True, False] Dump also DWH database (default: False)
ovirt_engine_db_dump_start_services: [True, False] Start engine and DWH service after dump (default: True)
ovirt_engine_db_dump_local_dir: directory on local machine where to store files (default: angine_dump in playbook directory)  
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
---
- hosts: engine
  vars:
    ovirt_engine_db_dump_dwh: True
  roles:
    - ovirt-engine-db-dump
```

Author Information
------------------

Lucie Leistnerova
lucie.leistnerova@gmail.com
