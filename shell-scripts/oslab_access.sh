#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "usage: script_name.sh ip_address root_password path_to_key"
    exit 1
fi

key_dir=$(dirname $0)/../artifacts
creds="root:$2"
ssh_flags="-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

# Enable root login
ssh $ssh_flags -qi $3 ec2-user@$1 -t sudo sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
ssh $ssh_flags -qi $3 ec2-user@$1 -t sudo sed -i 's/#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config
ssh $ssh_flags -qi $3 ec2-user@$1 -t sudo sed -i '/no-port-forwarding/d' /root/.ssh/authorized_keys
ssh $ssh_flags -qi $3 ec2-user@$1 -t "echo $creds | sudo chpasswd"
ssh $ssh_flags -qi $3 ec2-user@$1 -t sudo systemctl restart sshd.service

echo "Root login enabled with password $2 on machine $1"
