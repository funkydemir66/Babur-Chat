# ---------------------------

# Character

INVISIBLE = " "  # change this string with an invisible character

# Command

CMD = ":bc"

# ---------------------------

import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "Babur Chat",
    "description":"babur mucizesi :bc ac/kapa ile calisir.",
    "version": "0.1",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv)
ext.start()


on = False


def speech(msg):
    global on

    (text, bubble, idd) = msg.packet.read('sii')

    if on:
        if not text.startswith(CMD):
            msg.is_blocked = True
            message = ""

            for i in text:
                message += i + INVISIBLE

            ext.send_to_server('{out:Chat}{s:"%s"}{i:%s}{i:%s}' % (message, bubble, idd))

    if text == CMD + " ac":
        msg.is_blocked = True
        on = True
        ext.write_to_console('Babur Chat on')

    if text == CMD + " kapa":
        msg.is_blocked = True
        on = False
        ext.write_to_console('Babur Chat off')



ext.intercept(Direction.TO_SERVER, speech, 'Chat')
