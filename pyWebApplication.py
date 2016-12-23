#!/usr/bin/env python3

import sys
import os

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk, Gdk, WebKit

from GUI import Browser, Inspector
from WebServer import Server


if __name__ == '__main__':
    port = 60080

    script_dir = os.path.dirname(os.path.realpath(__file__))

    Gtk.init(sys.argv)

    server = Server(script_dir, port)

    browser = Browser()
    inspector = Inspector(browser.webview)

    browser.webview.load_uri("http://localhost:{}/".format(port))

    Gtk.main()
    server.stop()
