#!/bin/sh

sudo pacman -S cups gutenprint
yaourt -S cups-bjnp
sudo gpasswd -a $USER lp

sudo systemctl enable cups-browsed.service
sudo systemctl start cups-browsed.service
