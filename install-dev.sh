#!/bin/bash

INSTALL_ROOT="$HOME/.local/share/nemo-rsync"

mkdir -p "$INSTALL_ROOT"

ln -sfn "$PWD/backend" "$INSTALL_ROOT/backend"
ln -sfn "$PWD/extension" "$INSTALL_ROOT/extension"

mkdir -p ~/.local/share/nemo-python/extensions

ln -sfn \
"$INSTALL_ROOT/extension/nemo_rsync_extension.py" \
~/.local/share/nemo-python/extensions/nemo_rsync_extension.py