# -*- coding: utf-8 -*-

from __future__ import print_function
import js2py
import os
import shutil


def convert_path(path, path_from, path_to):
    dst = os.path.join(path_to, os.path.relpath(path, path_from))
    print (dst)
    if not os.path.exists(dst):
        os.makedirs(dst)
    for src in os.listdir(path):
        if src.startswith('.'):
            print(path, src, '[IGNORE]')
            continue
        src = os.path.join(path, src)
        dst = os.path.join(path_to, os.path.relpath(src, path_from))
        if os.path.isdir(src):
            convert_path(src, path_from, path_to)
        elif os.path.isfile(src):
            root, ext = os.path.splitext(dst)
            if ext == '.js':
                try:
                    js2py.translate_file(src, root + '.py')
                    print(dst, '[OK]')
                except js2py.base.PyJsException:
                    print(dst, '[ERROR]')
                    shutil.copyfile(src, dst)
            else:
                print(dst)
                shutil.copyfile(src, dst)


def main():
    bwipjs_path = os.path.abspath('../bwip-js')
    full_path = os.path.abspath('./bwip-py')
    convert_path(bwipjs_path, bwipjs_path, full_path)


if __name__ == '__main__':
    main()
