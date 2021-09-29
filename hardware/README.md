## Raspberry PI setup

Os : Raspberry PI OS Lite

- Create "ssh" file in the boot partition

- Create ```wpa_supplicant.conf``` file with the following content :
```
country=FR
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
}
```

- Start the Pi and connect over ssh

- Raspi config
    - ```sudo raspi-config```
    - Interface > enabled I2c
    - System Options > Boot > "Console AutoLogin"

- Update packages 
    - ```sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoclean && sudo apt-get autoremove```

- Install git / pip
    - ```sudo apt-get install git && sudo apt-get -y install python3-pip```

- Clone project (May need ssh key)
    - ```git@github.com:celian-rib/asso-card.git```

- Install docker
    - ```curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh```
    - ```sudo groupadd docker```
    - ```sudo usermod -aG docker $USER```

- Install touch screen driver (This will restart the pi)
    - ```git clone https://github.com/waveshare/LCD-show.git && ./LCD-show/LCD35B-show-V2```

- Install GUI components (https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup)
    - ```sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox```
    - ```sudo apt-get install --no-install-recommends chromium-browser```

    - En cas d'Erreur avec startx ```sudo mv /usr/share/X11/xorg.conf.d/99-fbturbo.conf ~```

    - Auto start point : ```sudo nano /etc/xdg/openbox/autostart```

- Fresh restart 
    - ```sudo reboot```

- (Optional) Install zsh
    - ```sudo apt install zsh```

    - Install oh my zsh because its looks cool 
    ```sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"```

    - Make hostname visible 
    ```echo "PROMPT='%{$fg_bold[cyan]%}$USER%{$fg_bold[blue]%}@%m%}%{$fg_bold[cyan]%} %c $(git_prompt_info)%{$reset_color%}'" >> ~/.zshrc```

## I2C setup

sudo apt install libnfc5 libnfc-bin libnfc-examples

## Wiring

TODO
