# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import sys, os, shutil
from pathlib import *

while True:
    cmd = input('%s>' % Path('.').resolve()).strip()
    if cmd == 'exit':
        sys.exit(0)
    elif cmd.startswith('dir'):
        params = cmd.split()
        if len(params) == 1:
            for filename in os.listdir(r'.'):
                print(filename)
        elif len(params) == 2:
            for filename in os.listdir(params[1]):
                print(filename)
        else:
            print('dir命令格式不正确，正确格式为: dir [路径]')
    elif cmd.startswith('cd'):
        params = cmd.split()
        if len(params) == 1:
            os.chdir(os.path.expanduser('~'))
        elif len(params) == 2 and Path(params[1]).is_dir():
            os.chdir(params[1])
        else:
            print('cd命令格式不正确，正确格式为: cd [路径]')
    elif cmd.startswith('md'):
        params = cmd.split()
        if len(params) < 2:
            print('md命令格式不正确，正确格式为: md <路径1> [路径2] ...')
        else:
            for i in range(1, len(params)):
                os.mkdir(params[i])
    elif cmd.startswith('copy'):
        params = cmd.split()
        if len(params) != 3 or (not Path(params[1]).is_file()) or (not Path(params[2]).is_dir()):
            print('copy命令格式不正确，正确格式为: copy <文件> <路径>')
        else:
            shutil.copy(params[1], params[2])
    elif cmd.startswith('move'):
        params = cmd.split()
        if len(params) != 3  or (not Path(params[1]).is_file()) or (not Path(params[2]).is_dir()):
            print('move命令格式不正确，正确格式为: move <文件> <路径>')
        else:
            shutil.move(params[1], params[2])
    else:
        print('无效命令')

        