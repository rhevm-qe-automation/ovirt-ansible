Role Name
=========

engine-setup with answerfile

By default engine-setup uses answer file specific for version of ovirt
(set in ovirt_engine_version) or you can specify own answer file in
ovirt_engine_answer_file_path.


Requirements
------------

Preinstalled clean environment with configured repositories

Role Variables
--------------

    ovirt_engine_type: Type of product
        'ovirt-engine' - for installing oVirt product
    ovirt_engine_version: Allowed version: [3.6, 4.0, 4.1]
    ovirt_engine_dwh: Bool value for installing local DWH

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


Dependencies
------------

Run common role first (for repositories)

Example Playbook
----------------

    hosts: engine
      remote_user: root
      vars:
        # role-vars: ovirt-common
          # ovirt_dependency_repo: ''
          # ovirt_repo: ''
        ovirt_rpm_repo: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release36.rpm'

        # role-vars: ovirt-engine-install-packages
        ovirt_engine_type: 'ovirt-engine'
        ovirt_engine_dwh: True
        ovirt_engine_version: 3.6

        # role-vars: ovirt-engine-setup
        ovirt_engine_hostname: 'engine.ovirt.org'

        ovirt_engine_db_host: 'localhost'
        ovirt_engine_db_port: 5432
        ovirt_engine_db_name: 'engine'
        ovirt_engine_db_user: 'engine'
        ovirt_engine_db_password: 'AqbXg4dpkbcVRZwPbY8WOR'
        ovirt_engine_dwh_db_host: 'localhost'
        ovirt_engine_dwh_db_port: 5432
        ovirt_engine_dwh_db_name: 'ovirt_engine_history'
        ovirt_engine_dwh_db_user: 'ovirt_engine_history'
        ovirt_engine_dwh_db_password: '37xmBKECANQGm0z3SfylMp'

      roles:
        - { role: common }
        - { role: engine-install }

Author Information
------------------

Petr Kubica
pkubica@redhat.com
