import os
from urllib import parse
f=open('heuristics.txt','r')
fa=open('rasaanalysis.txt','w+')
for i in f.readlines():
    fa.writelines(parse.unquote(i))
f.close()
fa.close()