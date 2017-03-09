oVirt guest-agent install package
=============================

This role installs ovirt-guest-agent package and
ensures the service is enabled and running.

Target Systems
--------------

* ovirt-guest


Requirements
------------

Configured ovirt repository.


Role Variables
--------------

```yaml
---
ovirt_guest_agent_pkg_prefix: "ovirt|rhevm|qemu"
```

Default value if variable not given is ```ovirt```.

Dependencies
------------

* ovirt-common

Example Playbook
----------------

```yaml
---
- hosts: ovirt-guest
  roles:
    - ovirt-guest-agent
```

Author Information
------------------

Katerina Koukiou
kkoukiou@redhat.com
