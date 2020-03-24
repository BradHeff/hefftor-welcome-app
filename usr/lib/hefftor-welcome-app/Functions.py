import base64
from pathlib import Path

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
