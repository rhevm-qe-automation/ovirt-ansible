Role Name
=========

Repository setup
Role install necessary repositories and update system

Requirements
------------

Preinstalled clean operating system.
Supported system are listed on


Role Variables
--------------

    ovirt_repo_file: list of repository files URL
    ovirt_repo: list of repository URL
    ovirt_rpm_repo: URL of RPM package with repository files

    Use any combination of ovirt_rpm_repo, ovirt_repo and ovirt_repo_file

Dependencies
------------

None

Example Playbook
----------------

```yaml
---
hosts: engine
  remote_user: root
  vars:
    # download repo file (list)
    ovirt_repo_file:
      -
        url: http://example.com/repository1.repo
        name: example.repo # default same as remote
        force: yes # default no
        # If force=yes, download the file and replace local file if the contents change.
        # If force=no, the file will only be downloaded if the destination does not exist.
      -
        url: http://example.com/repository2.repo

    # create repo file (list)
    ovirt_repo:
      -
        name: repo1
        url: http://example.com/path/to/packages
        enabled: yes # defualt yes

    # install from rpm (string)
    ovirt_rpm_repo: http://resources.ovirt.org/pub/yum-repo/ovirt-release36.rpm
  roles:
    - { role: common }
```

Author Information
------------------

Petr Kubica
pkubica@redhat.com
