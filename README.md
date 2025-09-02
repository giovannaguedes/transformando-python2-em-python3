# transformando-python2-em-python3
ferramenta que pega o script em python2 e transcreve para python3.

⚠️ Uso exclusivo para fins educacionais • Desenvolvido por M!ss s3c

📝 Guia passo a passo: Convertendo scripts

1. Abrir o script em Python2

No terminal, crie ou abra o arquivo:

nano script9.4.py


Adicione o seguinte código:

#!/usr/bin/python2
import urllib

site = urllib.urlopen("http://nome do site aqui.com.br/")
server = site.info()

print "O servidor web esta rodando"
print server['Server']

2. Executar a ferramenta de conversão

No terminal, rode:

2to3 -w script9.4.py


-w → faz a conversão e grava o arquivo atualizado.

3. Verificar os arquivos criados

No terminal:

ls script9*


Você verá algo assim:

script9.4.py        script9.4.py.bak


script9.4.py.bak → versão antiga em Python2.

script9.4.py → versão atualizada para Python3.

4. Ver a versão convertida

Abra a versão atualizada:

nano script9.4.py


Ela deve se parecer com isto:

#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error

site = urllib.request.urlopen("http://nome do site aqui.com.br/")
server = site.info()

print("O servidor web está rodando")
print(server['Server'])

👉 O que você aprendeu aqui

2to3 → ferramenta que converte scripts Python2 para Python3 automaticamente.

.bak → backup do script original em Python2.

urllib → mudou a forma de uso do Python2 para Python3 (urllib.request, urllib.parse, urllib.error).

print → agora é uma função em Python3.
