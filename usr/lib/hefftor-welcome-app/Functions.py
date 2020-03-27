# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import base64
from pathlib import Path
import os
import getpass
from os.path import expanduser
import threading

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()
user = "liveuser"

Settings = home + "/.config/hefftor-welcome-app/settings.conf"
Skel_Settings = "/etc/skel/.config/hefftor-welcome-app/settings.conf"
dot_desktop = "/usr/share/applications/hefftor-welcome-app.desktop"
autostart = home + "/.config/autostart/hefftor-welcome-app.desktop"
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/hefftor-welcome-app/"])


def keycode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position
