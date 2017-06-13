oVirt Engine Rename
===================

Role to rename to ovirt-engine

Target Systems
--------------

* engine

Requirements
------------

- Preinstalled clean environment with configured repositories and a working engine installation
- to have internally resolvable hostname using which we change the engine hostname to the new one

Role Variables
--------------

- `engine_new_fqdn`: would be the new engine-name that you want

Example Playbook
----------------

```yaml
---
- hosts: engine
  vars: 
    engine_new_fqdn: 'ovirt-rename-testing.gsoc.org'
  roles:
    - role: ovirt-engine-rename
```

Author Information
------------------

Tasdik Rahman
tasdik95@gmail.com