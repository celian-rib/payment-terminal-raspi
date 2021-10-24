# 1) Raspberry PI setup

Os : Raspberry PI OS Lite

***
- ### Before starting the pi :
    - Create a file named "ssh" in the boot disk (This enable ssh on boot)

    - Create ```wpa_supplicant.conf``` file on disk with the following content :
    ```
    country=FR
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    network={
        ssid="YOUR_NETWORK_NAME"
        psk="YOUR_PASSWORD"
    }
    ```
***
- ### Start the Pi and connect over ssh
    - ```ssh pi@192.168.x.xx``` (Default password is ```raspberry```)
***
- ### Update packages 
    - ```sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoclean && sudo apt-get autoremove```
***
- ### Install git / pip
    - ```sudo apt-get install git && sudo apt-get -y install python3-pip```
***
- ### Clone project (May need ssh key)
    - ```git@github.com:celian-rib/asso-card.git```
    - Créer fichiher ```.env```
***
- ### Install touch screen driver (This will restart the pi)
    - ```git clone https://github.com/waveshare/LCD-show.git```
    - ```cd ./LCD-show && ./LCD35-show```
***
- ### Install GUI components 
    [source](https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup)

    - ```sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox```
    - ```sudo apt-get install --no-install-recommends chromium-browser```
    - En cas d'Erreur avec startx ```sudo mv /usr/share/X11/xorg.conf.d/99-fbturbo.conf ~```
***
- ### Make the project auto start on boot
    - ```sudo raspi-config```
        - System Options > Boot > "Console AutoLogin"

    - Edit startup script with : ```sudo nano /etc/xdg/openbox/autostart``` (Executed when GUI drivers are ready)
        ```bash
        xset -dpms            # turn off display power management system
        xset s noblank        # turn off screen blanking
        xset s off            # turn off screen saver
        # Remove exit errors from the config files that could trigger a warning
        sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'
        sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences
        # Setup env
        export FLASK_ENV=production
        export PROD=True
        cd ~/asso-card
        git pull
        # Start backend app
        cd ~/asso-card/backend
        python3 src/app.py & >> ~/backend.log
        # Start hardware app
        cd ~/asso-card/hardware/src
        python3 app.py >> ~/hardware.log
        ```
***
- ### Fresh restart 
    - ```sudo reboot```
***
- ### (Optional) Install zsh (=better terminal)
    - ```sudo apt install zsh```

    - Install oh my zsh because its looks cool 
    ```sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"```

    - Make hostname visible 
    ```echo "PROMPT='%{$fg_bold[cyan]%}$USER%{$fg_bold[blue]%}@%m%}%{$fg_bold[cyan]%} %c $(git_prompt_info)%{$reset_color%}'" >> ~/.zshrc```

    - Disable ask-for-update prompt :
    ```nano ~/.zshrc```
        - decomment ```DISABLE_UPDATE_PROMPT="true"```

<br/>
<br/>
<br/>
<br/>

# 2) I2C setup
[(source)](https://www.youtube.com/watch?v=AUlefK47L0s)
***
- ### Activate I2C on raspberry :
    - ```sudo raspi-config```
        - Interface > enabled I2c
***
- ### Install i2c libs :
    - ```sudo apt install libnfc5 libnfc-bin libnfc-examples```
***
- ### Setup device :
    - ```sudo nano /etc/nfc/libnfc.conf```
        - Add at end of file : 
            ```
            device.name = "PN532 over I2C"
            device.connstring = "pn532_i2c:/dev/i2c-1"
            ```

<br/>
<br/>
<br/>
<br/>

# 3) Wiring

<img width="800px" src="https://github.com/celian-rib/asso-card/blob/main/hardware/img/i2c_wiring.png?raw=true" />
