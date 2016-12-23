from gi.repository import Gtk, WebKit

# thanks: https://gist.github.com/alex-eri/53518825b2a8a50dd1695c69ee5058cc
class Browser(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)

        self.connect("destroy", Gtk.main_quit)
        self.set_size_request(1200,700)

        self.webview = WebKit.WebView()
        #self.webview.load_uri("file:///{}/index.html".format(os.path.dirname(os.path.realpath(__file__))))

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.add(scrolled_window)
        scrolled_window.show_all()

        self.webview.connect('context-menu', self.callback)

        self.show()

    def callback(self, webview, context_menu, hit_result_event, event):
        option = Gtk.ImageMenuItem('Do it')
        option.connect('activate', self.option_activate_cb)
        context_menu.prepend(option)
        option.show()

    def option_activate_cb(self, image_menu_item):
        #self.webview.load_uri("javascript::alert('it works?');")
        self.webview.execute_script("alert('it works?');")
        print('It works.')
