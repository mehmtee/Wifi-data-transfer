#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import SimpleHTTPServer
import SocketServer
import os
import imp
from geter import*


print("""

	Hoşgeldiniz 

	1-) Localhost
	2-) Local Network

	""")
oku = str(input('>>>'))

print("""
	Port seçiniz
	[*ex] : 4423 9821,1954

	""")
port_oku = str(input('>>> '))

local_deger = port_oku
#localname
kod = ''

if oku =='1':
	kod = '127.0.0.1'
	serr = (('server = SocketServer.TCPServer(("127.0.0.1", {}), Handler)').format(local_deger))
if oku =='2':
	serr = (('server = SocketServer.TCPServer(("{}", {}), Handler)').format(local_name,local_deger))
	kod = local_name


class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
exec(serr)


print(("""
	

	Bağlantı Adresiniz : {}:{}

	""").format(kod,local_deger))
	

server.serve_forever()

