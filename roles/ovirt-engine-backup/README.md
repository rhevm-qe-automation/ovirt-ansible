Role Name
=========

Engine bakcup
Backup engine to archive file and download to client node

Requirements
------------

Pre-installed clean operating system.
Pre-installed and running ovirt.


Role Variables
--------------

    ovirt_backup_mode: backup'restore
    ovirt_backup_archive: Path to archive file
    ovirt_backup_log_file: Log file, downloaded in case of error
    ovirt_backup_scope: all|files|db|dwhdb|reportsdb
    
Dependencies
------------

None

Example Playbook
----------------

    hosts: engine
      remote_user: root
    vars:
        ovirt_backup_mode: 'backup'
        ovirt_backup_archive: '/tmp/engine-backup.gzip'
        ovirt_backup_log_file: '/tmp/engine-backup.log'
        ovirt_backup_scope: 'all'
    roles:
      - { role: ovirt-engine-bakcup }

Author Information
------------------

Lukas.Svaty
svatylukas@gmail.com
