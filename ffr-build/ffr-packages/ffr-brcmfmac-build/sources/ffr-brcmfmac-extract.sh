#!/bin/bash
IFS=$'\n'; for firmware in $(find /lib/firmware/cypress/ -name "*.xz"); do xzcat "$firmware" > "/lib/firmware/cypress/$(basename $firmware .xz)"; done
IFS=$'\n'; for firmware in $(find /lib/firmware/brcm/ -name "*.xz"); do xzcat "$firmware" > "/lib/firmware/brcm/$(basename $firmware .xz)"; done
