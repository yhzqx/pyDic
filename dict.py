#!/usr/bin/env python
# -*- coding:utf-8 -*-

# API key：273646050
# keyfrom：11pegasus11

import json
import sys
import sqlite3
import os
import sys

try:    # py3
    from urllib.parse import urlparse, quote, urlencode, unquote
    from urllib.request import urlopen
except:    # py2
    from urllib import urlencode, quote, unquote
    from urllib2 import urlopen

# conn = sqlite3.connect('test.db')


def fetch(query_str):
    # query_str = query_str.strip("'").strip('"').strip()
    # if not query_str:
        # query_str = 'python'

    # print(query_str)
    query = {
        'q': query_str
    }
    if query_str.find(" ") == -1:
        os.system('say ' + query_str)

    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + \
        urlencode(query)
    # print(str(url))
    try:
        response = urlopen(url, timeout=5)
        html = response.read().decode('utf-8')
    except Exception, e:
        print(str(e))
        return '{"errorCode":-1}'
    return html


def printYellowText(str):
    print('\033[1;33;40m' + str + '\33[0m')


def printBlueText(str):
    print('\033[1;36;40m' + str + '\33[0m')


def parseBasic(d):
    try:
        explains = d.get('basic').get('explains')
        printBlueText("单词释义：")
        for i in explains:
            printYellowText("   " + i)
    except:
        return


def parseTranslation(d):
    try:
        translation = d.get('translation')
        printBlueText("翻译：")
        for i in translation:
            printYellowText("   " + i)
    except:
        return


def parseWeb(d):
    try:
        web = d.get('web')
        printBlueText("网络释义：")
        for i in web:
            printYellowText("   " + i.get("key") + " ->")
            value = i.get("value")
            for k in value:
                printYellowText("      " + k)
    except:
        print(str(e))
        return


def parse(html):
    try:
        d = json.loads(html)
        if d.get('errorCode') == 0:
            parseTranslation(d)
            parseBasic(d)
            # parseWeb(d)
        elif d.get('errorCode') == -1:
            print('\033[1;31;40m翻译失败\33[0m')
        else:
            print('\033[1;31;40m无法翻译\33[0m')
    except:
        print('\033[1;31;40m解析错误\33[0m')
    print('')


def printHelp():
    print('输入关键字即可查询\n-h 呼出帮助\n-c 清屏\n-exit(or ctr+c) 退出程序')


def main():
    try:
        s1 = sys.argv[1].strip()
        if len(s1) == 0:
            print('\033[1;31;40m请输入查询内容\33[0m')
        elif s1 == '-h':
            printHelp()
        else:
            parse(fetch(s1))
    except IndexError:
        try:
            while True:
                s2 = raw_input().strip()
                if len(s2) == 0:
                    print('\033[1;31;40m请输入查询内容\33[0m')
                    print('')
                elif s2 == '-exit':
                    break
                elif s2 == '-c':
                    os.system('clear')
                elif s2 == '-h':
                    printHelp()
                else:
                    parse(fetch(s2))
        except KeyboardInterrupt:
            print(" 已退出")
            pass


if __name__ == '__main__':
    main()
