#/bin/bash
# needs to be run with sudo

if  [ -n "$(grep pdpserver /etc/hosts)" ]
then
    echo "pdpserver is already defined in /etc/hosts, skip.";
else
    echo "10.0.0.6\t pdpserver" >> /etc/hosts;
    echo "Setting up pdpserver to 10.0.0.6";
fi
