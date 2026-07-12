#!/usr/bin/env python3

from gi.repository import GObject, Nemo


class NemoRsyncExtension(GObject.GObject, Nemo.MenuProvider):

    def get_file_items(self, window, files):

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

    def on_rsync(self, menu, *args):

        print("Local rsync selected")


    def on_rsync_ssh(self, menu, *args):

        print("SSH rsync selected")