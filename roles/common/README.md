Role Name
=========

Repository setup

Requirements
------------

Preinstalled clean environment

Role Variables
--------------

    ovirt_repo: URL for main repository file 
    ovirt_dependency_repo: URL for dependency repository file
    ovirt_rpm_repo: URL for RPM package with repository files
    
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
