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

- Open config window and enable i2c in Interface settings
    - ```sudo raspi-config```

- Update packages 
    - ```sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoclean && sudo apt-get autoremove ```

- Install git 
    - ```sudo apt-get install git```

- Clone project (May need ssh key)
    - ```git@github.com:celian-rib/asso-card.git```


- (Optional) Install zsh
    - ```sudo apt install zsh```

    - Install oh my zsh because its looks cool 
    ```sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"```

    - Make hostname visible 
    ```echo "PROMPT='%{$fg_bold[cyan]%}$USER%{$fg_bold[blue]%}@%m%}%{$fg_bold[cyan]%} %c $(git_prompt_info)%{$reset_color%}'" >> ~/.zshrc```

- Fresh restart 
    - ```sudo reboot```

## I2C setup


## Wiring

TODO