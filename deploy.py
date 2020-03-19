import os
from datetime import date

commit_message = date.today()
content = "pelican content -o output -s pelicanconf.py"
output = "ghp-import output -b master"
master = "git push origin master"
commit = "git add . && git commit -m \"deploy {}\"".format(str(date.today()))
docs = "git push origin docs"

command = 'cmd /k "{} && {} && {} && {} && {}"'.format(content, output, master, commit, docs)

os.system(command)