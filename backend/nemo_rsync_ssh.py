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
    "rsync_runner_ssh.sh"
)

# gracefully exit if no files are supplied
if len(sys.argv) < 2:
    print("No source files were supplied.")
    sys.exit(1)

# Create a gtk dialog window.
dialog = Gtk.Dialog(
    title="Rsync to SSH"
)

dialog.add_buttons(
    Gtk.STOCK_CANCEL,
    Gtk.ResponseType.CANCEL,
    "Transfer",
    Gtk.ResponseType.OK,
)

# Create an empty dialogue window
content = dialog.get_content_area()

# sort the window contents as a grid
grid = Gtk.Grid()

# make the window entry labels
host_label = Gtk.Label(label="Host:")
user_label = Gtk.Label(label="Username:")
path_label = Gtk.Label(label="Destination:")
port_label = Gtk.Label(label="Port:")

# create the entry fields (gtk widgets)
host_entry = Gtk.Entry()
user_entry = Gtk.Entry()
path_entry = Gtk.Entry()
port_entry = Gtk.Entry()

host_entry.grab_focus()
port_entry.set_text("22")

# space out the grid
grid.set_row_spacing(6)
grid.set_column_spacing(6)
grid.set_border_width(12)

#attach labels and boxes in the grid then add the grid to the content box and show it
# grid.attach(    widget,    column,    row,    width,    height)

grid.attach(host_label, 0, 0, 1, 1)
grid.attach(host_entry, 1, 0, 1, 1)

grid.attach(user_label, 0, 1, 1, 1)
grid.attach(user_entry, 1, 1, 1, 1)

grid.attach(path_label, 0, 2, 1, 1)
grid.attach(path_entry, 1, 2, 1, 1)

grid.attach(port_label, 0, 3, 1, 1)
grid.attach(port_entry, 1, 3, 1, 1)
content.add(grid)
dialog.show_all()


# Wait until the user presses a button.
response = dialog.run()

if response == Gtk.ResponseType.OK:

# grab the input text from the dialog box
    host = host_entry.get_text()
    user = user_entry.get_text()
    remote_path = path_entry.get_text()
    port = port_entry.get_text()

    # get source files except the first item because python program is always the first item
    # Skip argv[0] (the Python script itself).
    sources = sys.argv[1:]

    launch_terminal(
        RUNNER_SCRIPT,
        *sources,
        host,
        user,
        port,
        remote_path
    )

else:
    print("Cancelled.")

dialog.destroy()