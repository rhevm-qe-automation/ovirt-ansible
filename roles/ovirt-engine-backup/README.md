oVirt Engine Backup
===================

Backups engine to archive file and download to client node

Target Systems
--------------

* engine
* dwh
* database

Requirements
------------

Pre-installed clean operating system.
Pre-installed and running ovirt.


Role Variables
--------------

```yaml
---
ovirt_backup_mode: backup'restore
ovirt_backup_archive: Path to archive file
ovirt_backup_log_file: Log file, downloaded in case of error
ovirt_backup_scope: all|files|db|dwhdb|reportsdb
```

Dependencies
------------

* [oVirt.engine-setup](https://galaxy.ansible.com/oVirt/engine-setup/)

Example Playbook
----------------

```yaml
---
- hosts: engine
  vars:
    ovirt_backup_mode: 'backup'
    ovirt_backup_archive: '/tmp/engine-backup.gzip'
    ovirt_backup_log_file: '/tmp/engine-backup.log'
    ovirt_backup_scope: 'all'
  roles:
      - ovirt-engine-bakcup
```

Author Information
------------------

Lukas.Svaty
svatylukas@gmail.com
