#!/usr/bin/env python3

import gi
import sys
import os

from backend.terminal_launcher import launch_terminal

# Tell Python we want GTK version 3.
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

# import location of whereever the rsync runner is actually located if the folder location changes and constants 
# determine the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# build the absolute path to the rsync_runner.sh
RUNNER_SCRIPT = os.path.join(
    SCRIPT_DIR,
    "rsync_runner.sh"
)

# gracefully exit if no files are supplied
if len(sys.argv) < 2:
    print("No source files were supplied.")
    sys.exit(1)

# Create a folder selection dialog.
dialog = Gtk.FileChooserDialog(
    title="Choose destination",
    action=Gtk.FileChooserAction.SELECT_FOLDER,
)

# Add the two buttons at the bottom.
dialog.add_buttons(
    Gtk.STOCK_CANCEL,
    Gtk.ResponseType.CANCEL,
    Gtk.STOCK_OK,
    Gtk.ResponseType.OK,
)

# Wait until the user presses a button.
response = dialog.run()

if response == Gtk.ResponseType.OK:

    destination = dialog.get_filename()

    # get source files except the first item because python program is always the first item
    # Skip argv[0] (the Python script itself).
    sources = sys.argv[1:]

    launch_terminal(
        RUNNER_SCRIPT,
        sources,
        destination
    )

else:
    print("Cancelled.")

dialog.destroy()