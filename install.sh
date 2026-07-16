#!/bin/bash

# ----------------------------------------
# Helper Functions
# ----------------------------------------

print_separator() {

    echo "------------------------------------------"

}

print_header() {

    echo
    echo "=========================================="
    echo "              Nemo Rsync"
    echo "=========================================="
    echo

}

error_exit() {

    echo
    echo "$1"
    echo
    echo "Installation cancelled."
    exit 1

}

# ----------------------------------------
# Start Installation
# ----------------------------------------

print_header

echo "Checking prerequisites..."
echo

# Check nemo-python
if ! dpkg -s nemo-python >/dev/null 2>&1
then

    error_exit \
"nemo-python is not installed.

Please install it first.

Linux Mint:
    Open Software Manager and search for:
        nemo-python

or install from the terminal:

    sudo apt install nemo-python"

fi

echo "✓ nemo-python found."

echo
print_separator

echo "Creating directories..."
echo

mkdir -p ~/.local/share/nemo-python/extensions
mkdir -p ~/.local/share/nemo-rsync

echo "✓ Directories ready."

echo
print_separator

echo "Installing extension..."
echo

cp -f \
    extension/nemo_rsync_extension.py \
    ~/.local/share/nemo-python/extensions/

echo "✓ Extension installed."

echo
print_separator

echo "Installing backend..."
echo

rm -rf ~/.local/share/nemo-rsync/backend

cp -r \
    backend \
    ~/.local/share/nemo-rsync/

echo "✓ Backend installed."

echo
print_separator

echo "Installation complete."
echo
echo "Restart Nemo by running:"
echo
echo "    nemo -q"
echo
echo "Then launch Nemo again."

print_separator