#!/usr/bin/env python3

from gi.repository import GObject, Nemo


class NemoRsyncExtension(GObject.GObject, Nemo.MenuProvider):

    def get_file_items(self, files):

        item = Nemo.MenuItem(
            name="NemoRsync::Test",
            label="Rsync Test",
            tip="Test Nemo Rsync extension"
        )

        item.connect("activate", self.on_test)

        return [item]

    def on_test(self, menu, *args):

        print("Hello from Nemo Rsync!")