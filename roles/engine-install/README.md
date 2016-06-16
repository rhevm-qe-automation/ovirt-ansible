Role Name
=========

Install clean engine

Requirements
------------

Preinstalled clean environment with configured repositories

Role Variables
--------------

    ovirt_repo: Main repository file 
    ovirt_dependency_repo: Dependency repository file
    ovirt_rpm_repo: Install repository files from RPM 
    
    Use either ovirt_rpm_repo or ovirt_dependency_repo, ovirt_rpm_repo
    
    engine_type: Allowed options are only 'ovirt' or 'rhevm'
    engine_answer_file_type: 
        '3.6_basic'  -   basic installation of engine with default options
        
    engine_hostname: FQDN of engine
    engine_organization: Organization
    engine_admin_password: admin@internal password

Dependencies
------------

Run common role first (for repositories)

Example Playbook
----------------

  hosts: engine
    remote_user: root
    vars:
      engine_type: 'ovirt'
      #ovirt_dependency_repo: ''
      #ovirt_repo: ''
      ovirt_rpm_repo: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release36.rpm'
      engine_answer_file_type: '3.6_basic'
      engine_hostname: 'engine.ovirt.org'
      engine_organization: 'ovirt.org'
      engine_admin_password: '123456'
    roles:
      - { role: common }
      - { role: engine-install }


Author Information
------------------

Petr Kubica
pkubica@redhat.com
