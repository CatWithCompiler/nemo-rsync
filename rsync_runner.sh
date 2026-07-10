#!/bin/bash

echo
echo "=== Nemo Rsync ==="
echo

# Last argument is always the destination.
destination="${@: -1}"

# Everything except the last argument are sources.
sources=("${@:1:$#-1}")

echo "Sources:"
printf '  %s\n' "${sources[@]}"

echo
echo "Destination:"
echo "  $destination"

echo
echo "Command:"
echo

rsync \
    -a \
    --info=progress2 \
    --human-readable \
    "${sources[@]}" \
    "$destination"

echo
echo "Press ENTER to close."

read