# Power Management

sudo pacman -S tlp

# Image viewer

´´´
sudo pacman -S feh
´´´


# Boot Menu Customization

convert splash.png -resize 1600x900 splash.png
convert splash.png -crop 1600x900+0+0 +repage splash.png

yaourt -S plymouth
sudo pacman -S ttf-dejavu

sudo vim /etc/mkinitcpio.conf
  add playmouth after udev
  replace encrypt with plymouth-encrypt

sudo mkinitcpio -p linux

## Plymouth Themeing

 **GOOGLE**


# Aur Package Installation

pacman -S base-devel git
git clone https://aur.archlinux.org/package-query.git
cd package-query
makepkg -si
cd ..
git clone https://aur.archlinux.org/yaourt.git
cd yaourt
makepkg -si
cd ..
rm -rf ./package-query
rm -rf ./yaourt


# NetworkManager

sudo pacman -S NetworkManager nm-applet dhclient

sudo vim /etc/NetworkManager/NetworkManager.conf
   add dhcp=dhclient to the [main] section
