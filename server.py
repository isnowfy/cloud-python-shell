# -*- coding: utf-8 -*-

import os
import time

import shell

if __name__ == '__main__':
    fin = 'server.txt'
    fout = 'client.txt'
    try:
        os.remove(fin)
        os.remove(fout)
    except:
        pass
    while True:
        if os.path.exists(fin):
            code = open(fin, 'r').read()
            os.remove(fin)
            f = open(fout, 'w')
            ret = shell.shell_handle(code)
            f.write(ret)
            f.close()
        time.sleep(0.1)
