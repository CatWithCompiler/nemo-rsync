#!/bin/bash

# ----------------------------------------
# Helper Functions
# ----------------------------------------

get_error_message() {

    case "$1" in

        23)
            echo "Some files or directories could not be transferred."
            ;;

        24)
            echo "Some source files disappeared during transfer."
            ;;

        12)
            echo "An error occurred while transferring data."
            ;;

        255)
            echo "SSH connection or authentication failed."
            ;;

        *)
            echo "An unknown error occurred."
            ;;

    esac

}

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

print_transfer_info() {
    echo "Sources:"
    echo

    for source in "${sources[@]}"
    do
        echo "    $source"
    done

    echo
    echo "Destination:"
    echo
    echo "    $destination"
}

# Comment out these options if checksums or compression behavior
# should use rsync's defaults
# Remove these options if they don't suit your workflow.
RSYNC_OPTIONS=(
    -a
    --info=progress2
    --human-readable
    --checksum-choice=xxh3
    --no-compress
)

# ----------------------------------------
# Parse Arguments
# ----------------------------------------

print_header


destination="${@: -1}"
sources=("${@:1:$#-1}")

print_transfer_info

echo
print_separator
echo "Starting transfer..."
print_separator
echo

# ----------------------------------------
# Start Transfer
# ----------------------------------------


rsync \
    "${RSYNC_OPTIONS[@]}" \
    "${sources[@]}" \
    "$destination"

result=$?

echo

print_separator

if [ "$result" -eq 0 ]; then
    echo "Transfer completed successfully."
    echo
    echo "Closing in 2 seconds..."
    echo
    print_separator

    sleep 2
    exit 0
fi

echo "Transfer failed."
echo

get_error_message "$result"

echo
echo "Error code: $result"

echo
echo "Press ENTER to close."
print_separator

read -r



