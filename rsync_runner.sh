#!/bin/bash

echo
echo "=== Rsync Runner ==="
echo

echo "Arguments received:"
echo

for arg in "$@"
do
    echo "$arg"
done

echo
echo "Press ENTER to close."

read