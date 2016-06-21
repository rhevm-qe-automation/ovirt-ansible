Role Name
=========

Install clean engine

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
         ovirt_engine_type: 'ovirt'
         ovirt_engine_answer_file_type: '3.6_basic'
         ovirt_engine_dwh: False
         ovirt_engine_hostname: 'engine.ovirt.org'
         ovirt_engine_organization: 'ovirt.org'
         ovirt_engine_admin_password: '123456'
    
       roles:
         - { role: common }
         - { role: engine-install }


Author Information
------------------

Petr Kubica
pkubica@redhat.com
