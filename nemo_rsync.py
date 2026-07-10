#!/usr/bin/env python3

import gi

from terminal_launcher import launch_terminal

# Tell Python we want GTK version 3.
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

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

    # Temporary test source.
    # Later Nemo will provide the selected files.
    sources = [
        __file__
    ]

    launch_terminal(
        "./rsync_runner.sh",
        sources,
        destination
    )

else:
    print("Cancelled.")

dialog.destroy()