#!/bin/sh

sudo pacman -Sy cups gutenprint
yaourt -Sy cups-bjnp
sudo gpasswd -a $USER lp

sudo systemctl enable cups-browsed.service
sudo systemctl start cups-browsed.service
