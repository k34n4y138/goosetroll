#!/bin/zsh

if [ ! -d "~/Library/.geezehidden/" ]
then
  git clone https://github.com/k34n4y138/goosetroll ~/Library/.geezehidden
  cd ~/Library/.geezehidden/ && zsh ~/Library/.geezehidden/setup.sh
else #executed for the second time inside the repo, time to reset memes]
  echo removing files
  rm -rf ~/Library/Containers/net.namedfork.DesktopGoose
  rm -rf ~/Library/.geezehidden/Contents/Resources/{Memes,Notes}
  python3 ~/Library/.geezehidden/main.py
fi
