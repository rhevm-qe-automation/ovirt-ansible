oVirt Engine Rename
===================

Role to change ovirt-engine fqdn and re-enroll all the related certificates

Target Systems
--------------

* engine

Requirements
------------

- Preinstalled clean environment with configured repositories and a working engine installation
- New internally resolvable hostname

Role Variables
--------------

- `ovirt_engine_rename_new_fqdn`: new ovirt-engine hostname

Example Playbook
----------------

```yaml
---
- hosts: engine
  vars: 
    ovirt_engine_rename_new_fqdn: 'ovirt-rename-testing.gsoc.org'
  roles:
    - role: ovirt-engine-rename
```

Author Information
------------------

Tasdik Rahman
tasdik95@gmail.com
