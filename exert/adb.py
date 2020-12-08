import os
import re


def get_devices():
    '''
    获取 
    '''

    with os.popen('adb devices') as p:
        r = []
        for line in p.readlines():
            m = re.match(r'^(.+?)\s+device\s+', line)
            if m != None:
                r.append(m[1])
        return r


def get_version(device=None):
    '''
    获取 Android 版本。
    '''

    c = f'adb -s {device} shell getprop ro.build.version.release' if device != None else 'adb shell getprop ro.build.version.release'
    with os.popen(c) as p:
        return p.readlines()[0].strip()
