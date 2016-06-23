Role Name
=========

install all necessary packages for engine (optional for DWH)

Requirements
------------

Preinstalled clean environment with configured repositories

Role Variables
--------------
    
    ovirt_engine_type: Type of product
        'ovirt-engine' - for installing oVirt product
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
        ovirt_engine_version: '3.6.7'
        ovirt_engine_version: 3.6.7
    
      roles:
        - { role: common }
        - { role: engine-install }

Author Information
------------------

Petr Kubica
pkubica@redhat.com
