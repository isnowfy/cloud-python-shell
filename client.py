# -*- coding: utf-8 -*-

import os
import time
import readline

import shell

if __name__ == '__main__':
    fin = 'client.txt'
    fout = 'server.txt'
    try:
        os.remove(fin)
        os.remove(fout)
    except:
        pass
    while True:
        code = raw_input('>>> ')
        f = open(fout, 'w')
        f.write(code)
        f.close()
        while True:
            if os.path.exists(fin):
                ret = open(fin, 'r').read()
                os.remove(fin)
                print ret
                break
            time.sleep(0.1)
