#!/usr/bin/env python3
# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import gi
import Functions as fn
import requests
import GUI
import subprocess
import webbrowser
import shutil
import socket
from time import sleep
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib  # noqa

REMOTE_SERVER = "www.google.com"


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title=fn.keycode("w5DDisOMw4zDqMOew6Q=",
                                                    "wr_CmsKqwqrDncOiw4FtwrzCmMOjwrjDmsK8wr3ChcOOwpvCvcKgw6bCosKpZMKqw6PCvw=="))
        self.set_border_width(10)
        self.set_default_size(750, 250)
        self.set_size_request(750, 250)
        self.set_icon_from_file(fn.os.path.join(
            fn.working_dir, 'images/hefftor-old.svg'))
        self.set_position(Gtk.WindowPosition.CENTER)
        self.results = None

        if not fn.os.path.exists(fn.home + "/.config/hefftor-welcome-app/"):
            fn.os.mkdir(fn.home + "/.config/hefftor-welcome-app/")
            with open(fn.Settings, "w") as f:
                f.write("autostart=True")
                f.close()

        GUI.GUI(self, Gtk, GdkPixbuf, subprocess, fn)

        if fn.username == fn.user:
            t = fn.threading.Thread(target=self.internet_notifier, args=())
            t.daemon = True
            t.start()

    def on_ai_clicked(self, widget):
        t = fn.threading.Thread(target=self.run_app,
                                args=(["pkexec", "/usr/bin/calamares"],))
        t.daemon = True
        t.start()

    def on_gp_clicked(self, widget):
        t = fn.threading.Thread(target=self.run_app,
                                args=(["/usr/bin/gparted"],))
        t.daemon = True
        t.start()

    def run_app(self, command):
        subprocess.call(command,
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    def statup_toggle(self, widget):
        if widget.get_active() is True:
            if fn.os.path.isfile(fn.dot_desktop):
                shutil.copy(fn.dot_desktop, fn.autostart)
        else:
            if fn.os.path.isfile(fn.autostart):
                fn.os.unlink(fn.autostart)
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(fn.Settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if fn.os.path.isfile(fn.Settings):
            with open(fn.Settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def on_link_clicked(self, widget, link):
        t = fn.threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_social_clicked(self, widget, event, link):
        t = fn.threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def weblink(self, link):
        webbrowser.open_new_tab(link)

    def is_connected(self):
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:  # noqa
            pass
        return False

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True

    def on_launch_clicked(self, widget, event, link):
        if fn.os.path.isfile("/usr/local/bin/arcolinux-tweak-tool"):
            t = fn.threading.Thread(target=self.run_app,
                                    args=("/usr/local/bin/arcolinux-tweak-tool",))
            t.daemon = True
            t.start()
        else:
            md = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.YES_NO,
                                   text="Not Found!")
            md.format_secondary_markup(
                "<b>ArcoLinux Tweak Tool</b> was not found on your system\n\
Do you want to install it?")

            result = md.run()

            md.destroy()

            if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
                t1 = fn.threading.Thread(target=self.installATT, args=())
                t1.daemon = True
                t1.start()

    def internet_notifier(self):
        while(True):
            if not self.is_connected():
                GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Not connected to internet</i></b> \nCalamares will <b>not</b> install additional software</span>")  # noqa
            else:
                GLib.idle_add(self.cc.set_text, "")
            sleep(3)

    def MessageBox(self, title, message):
        md = Gtk.MessageDialog(parent=self,
                               flags=0,
                               message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK,
                               text=title)
        md.format_secondary_markup(message)
        md.run()
        md.destroy()

    def installATT(self):
        subprocess.call(["pkexec",
                         "/usr/bin/pacman",
                         "-S",
                         "arcolinux-tweak-tool-git",
                         "--noconfirm"], shell=False)
        GLib.idle_add(self.MessageBox,
                      "Success!",
                      "<b>ArcoLinux Tweak Tool</b> has been installed successfully")  # noqa

    def get_message(self):
        t = fn.threading.Thread(target=self.fetch_notice,
                                args=())
        t.daemon = True
        t.start()

    def fetch_notice(self):
        try:
            url = 'https://bradheff.github.io/notice/notice'
            req = requests.get(url, verify=True, timeout=1)

            if req.status_code == requests.codes.ok:
                if not len(req.text) <= 1:
                    GLib.idle_add(self.vbox.pack_end, self.vbox2, False, False, 0)
                    GLib.idle_add(self.label4.set_text, req.text)
                    GLib.idle_add(self.vbox.show_all)
                    self.results = True
                    # print("FOUND")
                else:
                    self.results = False
                    # print("NOT LEN")
            else:
                self.results = False
                print("NOT OK")
        except:  # noqa
            print("EXCEPT")
            self.results = False


if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
