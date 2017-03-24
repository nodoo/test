# -*- coding: utf-8 -*-

from __future__ import print_function
import js2py
import os

def main():
    bwipjs_path = os.path.abspath('../bwip-js')
    full_path = os.path.abspath('.')
    print (full_path)
    js2py.translate_file(os.path.join(bwipjs_path, 'bwipjs.js'),
                         os.path.join(full_path, 'bwipjs.py'))

if __name__ == '__main__':
    main()