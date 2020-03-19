import os

content = "pelican content -o output -s pelicanconf.py"
listen = "pelican --listen"

command = 'cmd /k "{} && {}"'.format(content, listen)

os.system(command)