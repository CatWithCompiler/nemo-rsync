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
    -a \
    --info=progress2 \
    --human-readable \
    # Comment out using # checksum and lack of compression if they are not needed
    --checksum-choice=xxh3 \
    --no-compress \
    "${sources[@]}" \
    "$destination"

RESULT=$?

echo

print_separator

if [ "$RESULT" -eq 0 ]; then
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

echo "$(get_error_message "$RESULT")"

echo
echo "Error code: $RESULT"

echo
echo "Press ENTER to close."
print_separator

read



