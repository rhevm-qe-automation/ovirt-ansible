Role Name
=========

Repository setup

Requirements
------------

Preinstalled clean environment

Role Variables
--------------

    ovirt_repo: Main repository file 
    ovirt_dependency_repo: Dependency repository file
    ovirt_rpm_repo: Install repository files from RPM 
    
    Use either ovirt_rpm_repo or ovirt_dependency_repo, ovirt_rpm_repo
    
Dependencies
------------

None

Example Playbook
----------------

  hosts: engine
    remote_user: root
    vars:
      engine_type: 'ovirt'
      #ovirt_dependency_repo: ''
      #ovirt_repo: ''
      ovirt_rpm_repo: 'http://resources.ovirt.org/pub/yum-repo/ovirt-release36.rpm'

    roles:
      - { role: common }


Author Information
------------------

Petr Kubica
pkubica@redhat.com
