ovirt-iso-uploader-conf
=================================================

This role set config variables to oVirt upload ISO config file

Target systems
--------------

* any

Requirements
------------

oVirt repository configured


Role Variables
--------------

```yaml
---
ovirt_iso_uploader_user: username to use with the REST API
ovirt_iso_uploader_password: the oVirt Engine REST API password.
ovirt_iso_uploader_engine: hostname or IP address of the oVirt Engine
ovirt_iso_uploader_cert_file: CA certificate used to validate the engine.
ovirt_iso_uploader_iso_domain: the ISO domain to which the file(s) should be uploaded
ovirt_iso_uploader_nfs_server: the NFS server to which the file(s) should be uploaded.
ovirt_iso_uploader_ssh_user: the SSH user that the program will use for SSH file transfers.
ovirt_iso_uploader_ssh_port: the port to ssh and scp on
ovirt_iso_uploader_key_file: the identity file (private key) to be used for accessing the file server
```

Dependencies
------------

* [oVirt.repositories](https://galaxy.ansible.com/oVirt/repositories/)


Example Playbook
----------------

```yaml
---
- hosts: engine
  roles:
    - ovirt-iso-uploader-conf
```


Author Information
------------------

Meni Yakove
myakove@redhat.com
