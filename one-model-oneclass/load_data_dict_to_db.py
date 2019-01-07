import json

import requests
from urllib import parse
import psycopg2
import time
classnames=set()
classnames.add('salaryslip')
classnames.add('salaryrelease')
classnames.add('salarybreakup')
classnames.add('itform')
classnames.add('form16')
classnames.add('None')
conn=psycopg2.connect("dbname=tl_backup user=sayint host=bot.sayint.ai port=5433 password=smartinsights")
cur=conn.cursor()
cur1=conn.cursor()
conn.autocommit=True
fh=0
with open('testpyt.txt','r') as tpt:
    fh=json.load(tpt)
    print(len(fh))
for i,j in fh.items():
    print(j)
scores=fh
for keyid,keyvalue in scores.items():
    cur1.execute('select a.multi_class,a.classes_tsv from emails.analytics a,emails.tracker t where a.msg_id=t.msg_id and t.msg_id=\'{0}\''.format(keyid))
    result=cur1.fetchall()
    aresult="".join(i.replacerrore('\'','')+' ' for i in result[0][1].split(' '))
    stringtop=''
    for i,j in keyvalue.items():
        if i in classnames:
            stringtop=stringtop+i+'='+str(j)+' '
    cur.execute('insert into luis_summary values(\'{0}\',\'{1}\',{2},\'{3}\',\'{4}\',\'{5}\')'.format(keyid,keyvalue['message'],result[0][0],aresult,keyvalue['top'],stringtop))
