#!/bin/bash
# `toxworkdir` and `toxinidir` must be past as parametrs (in this order)!
if [ $# -ne 2 ]; then
  echo "'{toxworkdir}' and '{toxinidir}' must be past as parameters to this script (in this order)"
  exit 1
fi;

TOXWORKDIR=$1
TOXINIDIR=$2

# Create one playbook for every role
mkdir -p ${TOXWORKDIR}/playbooks
for path_role in ${TOXINIDIR}/roles/*; do
  if [ -d "${path_role}" ]; then
      role=`echo ${path_role} | sed 's/.*\///'` # directory name only
      echo -e "---\nremote_user: root\nroles:\n  - {role: ${role}}\n" > ${TOXWORKDIR}/playbooks/${role}.yml
  fi;
done

# Test ansible-lint for every created playbook
ansible-lint ${TOXWORKDIR}/playbooks/*.yml
