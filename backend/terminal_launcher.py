#!/usr/bin/env python3

import subprocess
import shutil

SUPPORTED_TERMINALS = {
    "kitty": ["sh", "-c"],
    "gnome-terminal": ["--"],
    "xfce4-terminal": ["-x"],
    "mate-terminal": ["-x"],
    "konsole": ["-e"],
    "tilix": ["-e"],
    "x-terminal-emulator": ["-e"],
    "xterm": ["-e"],
}

def find_terminal():
    """
    Returns:
        (terminal_name, launch_arguments)
        or
        (None, None)
    """

    for terminal, args in SUPPORTED_TERMINALS.items():
        if shutil.which(terminal):
            return terminal, args

    return None, None

def launch_terminal(script, *arguments):

    terminal, launch_args = find_terminal()

    if terminal is None:
        print("No supported terminal emulator found.")
        return

    command = (
        [terminal]
        + launch_args
        + [script]
        + list(arguments)
    )

    print("Launching:")
    print(" ".join(command))

    subprocess.Popen(command)

