#!/bin/bash

#Creates symlinks to your working project folder in the nemo-python plugins directory
mkdir -p ~/.local/share/nemo-python/extensions

ln -sf \
"$PWD/extension/nemo_rsync_extension.py" \
~/.local/share/nemo-python/extensions/

mkdir -p ~/.local/share/nemo-rsync

ln -sfn \
"$PWD/backend" \
~/.local/share/nemo-rsync/backend