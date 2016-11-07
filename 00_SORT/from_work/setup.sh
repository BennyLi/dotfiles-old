#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#####  SOFTWARE  #####

sudo pacman -Sy --needed wget

# SQLDeveloper
# Can only be downloaded after logging in with an Oracle account
#cd /tmp
#wget -O sqldeveloper.zip http://download.oracle.com/otn/java/sqldeveloper/sqldeveloper-4.1.5.21.78-no-jre.zip
#unzip sqldeveloper.zip -d /opt/sqldeveloper


#####  LINK  #####
function link_file {
    local src=$1
    local dest=$2
    if [ -f $dest ]; then
        sudo cp $dest $dest.bak
    fi
    sudo ln -s $src $dest
}   

link_file $SCRIPT_DIR/.config/i3/config /home/bln/.config/i3/config
link_file $SCRIPT_DIR/etc/vconsole.conf /etc/vconsole.conf

if [ -d /opt/sqldeveloper ]; then
    link_file $SCRIPT_DIR/apps-conf/sqldeveloper/sqldeveloper.conf /opt/sqldeveloper/sqldeveloper/bin/sqldeveloper.conf
fi

for f in bin/*; do
    link_file $SCRIPT_DIR/$f /usr/local/$f
done

exit

#####  ICON THEMES  #####

sudo pacman -Sy --needed hicolor-icon-theme
cd /opt
sudo git clone https://github.com/erikdubois/Super-Ultra-Flat-Numix-Remix
cd Super-Ultra-Flat-Numix-Remix
for theme in */; do
    echo "Installing icon theme ${theme%/} ..."
    sudo rm -rf /usr/share/icons/$theme
    sudo cp -R $(pwd)/$theme /usr/share/icons/
    sudo gtk-update-icon-cache -f -t /usr/share/icons/$theme
done
