#!/bin/python3
from os import path
from core.functions import check_root, command, check_tor, get_info
from core.banner import banner
from core.tools import install, anonymous, search, check_urls, scan, update, about


check_root()

install()

check_tor()

while True:
    print('')
    tor = get_info()[0]
    try:
        banner(tor)
        cmd = command()

        if cmd == 1:
            anonymous()

        elif cmd == 2:
            search()

        elif cmd == 3:
            check_urls()

        elif cmd == 4:
            scan()

        elif cmd == 5:
            update()

        elif cmd == 6:
            about()

        elif cmd == 0:
            break

    except KeyboardInterrupt:
        break
    except:
        continue
