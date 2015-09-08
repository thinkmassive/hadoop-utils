#!/bin/bash

# Install Kerberos packages
yum install -y krb5-server krb5-libs krb5-workstation

# Set Sandbox as KDC
sed -i /etc/krb5.conf 's/kerberos.example.com/sandbox.hortonworks.com/g'

# Create Kerberos database
kdb5_util create -s

# Start KDC & kadmin
/etc/rc.d/init.d/krb5kdc start
/etc/rc.d/init.d/kadmin start

# Auto-start on boot
chkconfig krb5kdc on
chkconfig kadmin on

# Create KDC admin principal
kadmin.local -q "addprinc admin/admin"
