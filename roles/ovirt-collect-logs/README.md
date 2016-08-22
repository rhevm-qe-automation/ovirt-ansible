Collect logs from oVirt deployment
==================================

This role collects relevant logs from oVirt deployment members.


Requirements
------------

None


Role Variables
--------------

```yaml
---
ovirt_collect_logs_from_system: "engine|hypervisor|db|dwh"
```

Dependencies
------------

None


Example Playbook
----------------

```yaml
---
hosts: engine
  roles:
    -
      role: "ovirt_collect_logs"
      ovirt_collect_logs_from_system: "engine"
```


Author Information
------------------

Lukas Bednar
lbednar@redhat.com
