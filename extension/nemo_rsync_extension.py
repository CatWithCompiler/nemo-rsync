#!/usr/bin/env python3
import subprocess
import os
import gi

from gi.repository import Gtk

# unquote allows parsing of filenames properly from the NemoVFSFille object URI
from urllib.parse import urlparse, unquote

from gi.repository import GObject, Nemo

# import location of whereever the extension is actually located if the folder location changes and constants 
# determine the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

#setting debug to True prints debug information
DEBUG = False

VERSION = "2.0.0"

# define methods in class
class NemoRsyncExtension(GObject.GObject, Nemo.MenuProvider):

    # function to get names and parse them
    def get_selected_paths(self):

        paths = []

        for file in self.files:

            uri = file.get_uri()

            path = unquote(
                urlparse(uri).path
            )

            paths.append(path)

        return paths


    #function to launch backend
    def launch_backend(self, module_name):

        sources = self.get_selected_paths()

        command = [
            "python3",
            "-m",
            module_name,
            *sources
        ]

# Debug output
        if DEBUG:
            print("PROJECT_ROOT =", PROJECT_ROOT)
            print("COMMAND =", command)

        subprocess.Popen(
            command,
            cwd=PROJECT_ROOT
        )
#menu entry and submenus
    def get_file_items(self, window, files):

        self.files = files

# Debug output
        if DEBUG:
            print("get_file_items() called")

        rsync_item = Nemo.MenuItem(
            name="NemoRsync::Root",
            label="Rsync",
            tip="Rsync operations"
        )

        submenu = Nemo.Menu()

        local_item = Nemo.MenuItem(
            name="NemoRsync::Local",
            label="Rsync to...",
            tip="Copy files using rsync"
        )

        ssh_item = Nemo.MenuItem(
            name="NemoRsync::SSH",
            label="Rsync to SSH...",
            tip="Copy files over SSH"
        )

        about_item = Nemo.MenuItem(
            name="NemoRsync::About",
            label="About Nemo Rsync...",
            tip="About this extension"
        )

        about_item.connect(
            "activate",
            self.on_about
        )

        local_item.connect("activate", self.on_rsync)

        ssh_item.connect("activate", self.on_rsync_ssh)

        submenu.append_item(local_item)
        submenu.append_item(ssh_item)
        submenu.append_item(about_item)

        rsync_item.set_submenu(submenu)

        return [rsync_item]

    def on_rsync(self, menu):
        self.launch_backend("backend.nemo_rsync")


    def on_rsync_ssh(self, menu):

        self.launch_backend("backend.nemo_rsync_ssh")


    def on_about(self, menu):

        dialog = Gtk.AboutDialog()

        dialog.set_program_name("Nemo Rsync")
        dialog.set_version(VERSION)
        dialog.set_comments("Simple right-click rsync integration for Nemo.")
        dialog.set_authors([
            "https://github.com/CatWithCompiler"
        ])

        dialog.set_comments(
            "Developed with extensive assistance from ChatGPT (deal with it!)."
        )

        dialog.set_license_type(Gtk.License.MIT_X11)
        dialog.set_website("Placeholder")

        dialog.run()
        dialog.destroy()