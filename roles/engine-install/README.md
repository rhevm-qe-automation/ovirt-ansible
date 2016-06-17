Role Name
=========

Install clean engine

Requirements
------------

Preinstalled clean environment with configured repositories

Role Variables
--------------

    ovirt_repo: URL for main repository file 
    ovirt_dependency_repo: URL for dependency repository file
    ovirt_rpm_repo: URL for RPM package with repository files
    
    Use either ovirt_rpm_repo or ovirt_dependency_repo, ovirt_rpm_repo
    
    engine_type: Allowed options are only 'ovirt' or 'rhevm'
    engine_answer_file_type: 
        '3.6_basic'  -   basic installation of engine 3.6 with default options
        '4.0_basic'  -   basic installation of engine 4.0 with default options
    engine_dwh: Bool value for installing DWH (local - not need special answerfile)   
    engine_hostname: engine FQDN
    engine_organization: Organization domain
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
      engine_dwh: False
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
