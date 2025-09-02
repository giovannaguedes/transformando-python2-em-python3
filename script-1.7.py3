#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error

site = urllib.request.urlopen("http://nome do site aqui.com.br/")

server = site.info()

print("0 servidor web esta rodando")

print(server['Server']) 
