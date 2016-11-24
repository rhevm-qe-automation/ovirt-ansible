oVirt engine config
===================

This role allows tune installed engine using ``engine-config`` CLI tool.

Target systems
--------------

* engine

Requirements
------------

oVirt installed and running.


Role Variables
--------------

You can specify options one by one.

```yaml
---
ovirt_engine_config:
  -
    key: "option name"
    value: "option value"
    version: desired-version
```

Or specify set of options in property file.
This way is preferable when you want to set passwords.

```yaml
---
ovirt_engine_config_property_file: "properties content"
```


Dependencies
------------

None


Example Playbook
----------------

```yaml
---
- hosts: engine
  remote_user: root
  vars:
    ovirt_engine_config:
      -
        key: "EnableMACAntiSpoofingFilterRules"
        value: false
        version: "general"
  roles:
    -
      role: "ovirt-engine-config"
```


Author Information
------------------

Lukas Bednar
lbednar@redhat.com
