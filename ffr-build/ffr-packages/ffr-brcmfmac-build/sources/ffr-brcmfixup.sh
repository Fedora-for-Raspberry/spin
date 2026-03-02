#!/bin/bash
iw dev wlan0 set power_save off
btmgmt -i hci0 power off
btmgmt -i hci0 public-addr $(cat /sys/class/net/e*0/address | sort | head -n1)
btmgmt -i hci0 power on