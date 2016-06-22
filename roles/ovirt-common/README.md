Role Name
=========

Repository setup
Role install necessary repositories

Requirements
------------

Preinstalled clean operating system.
Supported system are listed on


Role Variables
--------------

    ovirt_engine_type: Type of product
        'ovirt-engine' - for installing oVirt product
        'rhevm' - for installing RHEVM
    ovirt_repo: URL of main repository file 
    ovirt_dependency_repo: URL of dependency repository file
    ovirt_rpm_repo: URL of RPM package with repository files
    
    Use either ovirt_rpm_repo or ovirt_dependency_repo, ovirt_rpm_repo
    
Dependencies
------------

None

Example Playbook
----------------

    hosts: engine
      remote_user: root
      vars:
        ovirt_engine_type: 'ovirt-engine'
        #ovirt_dependency_repo: ''
        #ovirt_repo: ''
        ovirt_rpm_repo: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release36.rpm'

    roles:
      - { role: common }


Author Information
------------------

Petr Kubica
pkubica@redhat.com
