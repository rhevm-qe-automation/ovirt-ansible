Role Name
=========

Remote DB setup
- install and configure PostgreSQL server on machine (latest from repository) 
- create necessary roles and databases for engine and DWH (based on variables)
- update firewalld and iptables (based on service present)

- If PostgreSQL server is already installed then create only roles and databases

Requirements
------------

Preinstalled clean operating system.

Role Variables
--------------

    # vars for PostgreSQL
    ovirt_engine_remote_db_port: PostgreSQL port for listening (default: 5432)
    ovirt_engine_remote_db_listen_address: Listen address (default '*')
    
    ovirt_engine_remote_db: [yes, no] Create engine database
    ovirt_engine_dwh_remote_db: [yes, no] Create DWH database
    
    # vars for databases and roles
    ovirt_engine_db_name: DB name for ovirt-engine (default: 'engine')
    ovirt_engine_db_user: DB user which can access ovirt-engine DB (default: 'engine')
    ovirt_engine_db_password: password for user of ovirt-engine DB
    ovirt_engine_dwh_db_name: DB name for ovirt-engine-dwh (default: 'ovirt_engine_history')
    ovirt_engine_dwh_db_user: DB user which can access ovirt-engine-dwh DB (default: 'ovirt_engine_history')
    ovirt_engine_dwh_db_password: password for user of ovirt-engine DB
    
Dependencies
------------

None

Example Playbook
----------------

    hosts: database
      remote_user: root
      vars:
        # vars for PostgreSQL
        ovirt_engine_remote_db_port: 5432
        ovirt_engine_remote_db_listen_address: '*'
        
        ovirt_engine_remote_db: yes
        ovirt_engine_dwh_remote_db: yes
        
        # vars for databases and roles
        ovirt_engine_db_name: 'engine'
        ovirt_engine_db_user: 'engine'
        ovirt_engine_db_password: 123456
        ovirt_engine_dwh_db_name: 'ovirt_engine_history'
        ovirt_engine_dwh_db_user: 'ovirt_engine_history'
        ovirt_engine_dwh_db_password: 123456

    roles:
      - { role: ovirt-engine-remote-db }

Author Information
------------------

Petr Kubica
pkubica@redhat.com
