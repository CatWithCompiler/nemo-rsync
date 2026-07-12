#!/usr/bin/env python3
import subprocess
import os

# unquote allows parsing of filenames properly from the NemoVFSFille object URI
from urllib.parse import urlparse, unquote

from gi.repository import GObject, Nemo

# import location of whereever the extension is actually located if the folder location changes and constants 
# determine the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)



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

        subprocess.Popen(
            command,
            cwd=PROJECT_ROOT
        )
#menu entry and submenus
    def get_file_items(self, window, files):

        self.files = files

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

        local_item.connect("activate", self.on_rsync)

        ssh_item.connect("activate", self.on_rsync_ssh)

        submenu.append_item(local_item)
        submenu.append_item(ssh_item)

        rsync_item.set_submenu(submenu)

        return [rsync_item]

    def on_rsync(self, menu):
        self.launch_backend("backend.nemo_rsync")


    def on_rsync_ssh(self, menu):

        self.launch_backend("backend.nemo_rsync_ssh")