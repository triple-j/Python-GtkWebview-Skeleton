from gi.repository import Gtk, WebKit

# thanks: https://gist.github.com/alex-eri/53518825b2a8a50dd1695c69ee5058cc
class Inspector(Gtk.Window):
    def __init__(self, view, *args, **kwargs):
        super(Inspector, self).__init__(*args, **kwargs)
        self.set_size_request(1200,700)
        self.webview = view
        settings = WebKit.WebSettings()
        settings.set_property('enable-developer-extras', True)
        view.set_settings(settings)


        self.webview = WebKit.WebView()
        self.inspector = view.get_inspector()

        self.inspector.connect("inspect-web-view", self.inspect)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.add(self.scrolled_window)
        self.scrolled_window.show()

        self.webview = WebKit.WebView()
        self.scrolled_window.add(self.webview)



    def inspect(self,inspector,view,*a,**kw):
        self.scrolled_window.show_all()
        self.show()
        return self.webview
