#!/bin/sh

LHT_PROXY_SERVER=57.20.4.150

if ping -c 1 $LHT_PROXY_SERVER &> /dev/null
then
    echo 0
else
    echo 1
fi
