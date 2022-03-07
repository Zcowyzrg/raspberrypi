#!/bin/sh

if therm=$(ls /sys/bus/w1/devices/28-*/w1_slave)
then
    perl -nle 'if (/t=([0-9]+)/) {print $1 / 1000.0}' < $therm
fi
