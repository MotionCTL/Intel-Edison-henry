#!/bin/sh

dmesg -n 3
echo mode1 > /sys/kernel/debug/gpio_debug/gpio27/current_pinmux
echo mode1 > /sys/kernel/debug/gpio_debug/gpio28/current_pinmux
