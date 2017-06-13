oVirt Engine Rename
===================

Role to rename ovirt-engine and re-enroll all the related certificates

Target Systems
--------------

* engine

Requirements
------------

- Preinstalled clean environment with configured repositories and a working engine installation
- To have internally resolvable hostname using which we change the engine hostname to the new one

Role Variables
--------------

- `ovirt_engine_rename_new_fqdn`: would be the new engine-name that you want

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