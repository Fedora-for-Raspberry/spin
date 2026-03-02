#!/bin/bash
# gencmdline produces ROOTSPEC cmdlines, modify via other FfR utilities
cat /proc/cmdline | sed -rE 's/root=.*? rootwait/quiet rw rootwait rootfstype=ext4 ROOTSPEC/g' | sed 's/reboot=w //g' | sed 's/ ro / rw /g'
