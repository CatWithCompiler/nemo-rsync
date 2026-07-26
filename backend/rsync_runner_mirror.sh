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
    echo "              Nemo Mirror"
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

# These options are tuned for fast local transfers.
# Remove them if they don't suit your workflow or if you prefer
# rsync's default checksum and compression behavior.
RSYNC_OPTIONS=(
    -a
    --delete
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

# to remove the pause for confirmation comment out the following block of code.
echo
print_separator
echo "WARNING! Mirroring can delete data at the target location as part of the mirroring process."
echo "Please make sure your data is appropriately backed up against to protect against data loss."
print_separator
echo "Press ENTER to begin the mirroring transfer."
print_separator
read -r

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



