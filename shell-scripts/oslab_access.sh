#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "usage: script_name.sh ip_address"
    exit 1
fi

key_dir=$(dirname $0)/../artifacts


# Enable root login
ssh -qi $key_dir/OSLab_ssh_key.private ec2-user@$1 -t sudo sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
ssh -qi $key_dir/OSLab_ssh_key.private ec2-user@$1 -t sudo sed -i 's/#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config
ssh -qi $key_dir/OSLab_ssh_key.private ec2-user@$1 -t sudo sed -i '/no-port-forwarding/d' /root/.ssh/authorized_keys
ssh -qi $key_dir/OSLab_ssh_key.private ec2-user@$1 -t echo "root:qum5net" | sudo chpasswd
ssh -qi $key_dir/OSLab_ssh_key.private ec2-user@$1 -t sudo systemctl restart sshd.service

echo "Root login enabled with password qum5net on machine $1"
