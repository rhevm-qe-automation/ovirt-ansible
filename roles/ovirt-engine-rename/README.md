oVirt Engine Rename
===================

Generate answerfile and run engine-setup with it.

Target Systems
--------------

* engine

Requirements
------------

Preinstalled clean environment with configured repositories and a working engine installation

Role Variables
--------------

- `ansible_fqdn`: would be the new engine-name that you want

Example Playbook
----------------

```yaml
---
- hosts: engine
  vars: 
    ansible_fqdn: 'ovirt-rename-testing.gsoc.org'
  roles:
    - role: ovirt-engine-rename
```

Author Information
------------------

Tasdik Rahman
tasdik95@gmail.com