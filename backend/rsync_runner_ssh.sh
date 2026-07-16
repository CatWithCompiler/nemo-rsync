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

    echo "Host:        $host"
    echo "User:        $user"
    echo "Port:        $port"
    echo "Remote path: $remote_path"
    echo "SSH target:  $remote"

    echo
    echo "Sources:"

    for source in "${sources[@]}"
    do
        echo "    $source"
    done

}

# These options are tuned for fast local transfers.
# Remove them if they don't suit your workflow or if you prefer
# rsync's default checksum and compression behavior.
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


remote_path="${@: -1}"
port="${@: -2:1}"
user="${@: -3:1}"
host="${@: -4:1}"

sources=("${@:1:$#-4}")

remote="${user}@${host}:${remote_path}"

print_transfer_info

# to remove the pause for confirmation comment out the following block of code.
echo
print_separator
echo "Press ENTER to begin the transfer."
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
    -e "ssh -p $port" \
    "${sources[@]}" \
    "$remote"

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



