Role Name
=========

engine-setup with answerfile

Requirements
------------

Preinstalled clean environment with configured repositories

Role Variables
--------------
    
    ovirt_engine_type: Allowed options are only 'ovirt-engine' or 'rhevm'
    ovirt_engine_version: Allowed version: [3.6.x, 4.0.x]
    ovirt_engine_dwh: Bool value for installing DWH (local - not need special answerfile)   
    
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
        ovirt_engine_version: 3.6.x
        
        # role-vars: ovirt-engine-setup
        ovirt_engine_answer_file_type: '3.6_basic'
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
