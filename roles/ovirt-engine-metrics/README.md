oVirt Engine Metrics
====================

Setting up engine metrics 

Target systems
--------------

* engine

Requirements
------------

Preinstalled clean environment with configured repositories.

Dependencies
------------

* TODO

Assumptions
-----------

- allow connections on the following ports/protocols: icmp (for ping), tcp ports 22, 80, 443, 8443 (openshift console), 24284 (secure_forward) on the VM where metrics is to be setup, which would be seperate from where ovirt-engine is installed
- you have `root` ssh access, or a user who can ssh into without password

Author
------

Tasdik Rahman
tasdik95@gmail.com
