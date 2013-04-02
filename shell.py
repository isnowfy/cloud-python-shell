# -*- coding: utf-8 -*-

import os
import sys
import readline
import cStringIO
import traceback

env = None

class IOHandler(object):
    def __init__(self):
        self.io = cStringIO.StringIO()

    def __enter__(self):
        self.old_out = sys.stdout
        self.old_err = sys.stderr
        sys.stdout = self.io
        sys.stderr = self.io
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.old_out
        sys.stderr = self.old_err

    def get_out(self):
        return self.io.getvalue() or ''

def shell_handle(code):
    global env
    if code == 'clear' or not env:
        env = {}
    if code == 'clear':
        return 'clear is successful'
    ret = ''
    with IOHandler() as handle:
        try:
            exec(code, env)
            ret = handle.get_out()
        except:
            return traceback.format_exc()
    if not ret:
        with IOHandler() as handle:
            try:
                exec('print %s' % code, env)
                ret = handle.get_out()
            except:
                pass
    return ret

if __name__ == '__main__':
    while True:
        code = raw_input('>>> ')
        print shell_handle(code)
