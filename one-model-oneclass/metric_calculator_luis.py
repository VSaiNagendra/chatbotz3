import json
import time
import requests
from urllib import parse
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '7a59937e80dd423fa5415fdbd8289275',
}
countoferrors=0
ssdic={'name':'salaryslip','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
srdic={'name':'salaryrelease','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
sbdic={'name':'salarybreakup' ,'true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
itdic={'name':'itform', 'true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
fdic={'name':'form16','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
filenames=['form16','itform','salarybreakup','salaryrelease','salaryslip']
listdic=[fdic,itdic,sbdic,srdic,ssdic]
count=0
fa=open('analysisoutput','w+')
for l in filenames:
    fa.write('\n----------------------------------'+str(l)+'------------------------------------------\n')
    fa.write('\n')
    with open('{0}test'.format(l),'r+') as fread:
            for line in fread.readlines():
                time.sleep(0.3)
                if line=='\n':
                    count+=1
                    continue
                line = parse.quote(line)
                params = {
                    # Query parameter
                    'example': '{0}'.format(line.encode("utf-8")),
                    # Optional request parameters, set to default values
                    'subscription-Key':'7a59937e80dd423fa5415fdbd8289275',
                }
                r=requests.get('https://westus.api.cognitive.microsoft.com/luis/webapi/v2.0/apps/0f064452-364c-4f0f-a0f1-f64bf2deca70/versions/0.1/predict?subscription-key=7a59937e80dd423fa5415fdbd8289275&example={0}&patternDetails=true'.format(line))
                print(r.status_code)
                if(int(r.status_code)>=400):
                    print('error '+str(countoferrors)+' '+line)
                    countoferrors+=1
                    continue
                r=r.json()
                print(parse.unquote(line))
                print(r["intentPredictions"][0]["name"])
                if l==r["intentPredictions"][0]["name"]:
                    for dic in listdic:
                        if dic['name']==l:
                            dic['true']['positive']+=1
                        else:
                            dic['true']['negative']+=1
                else:
                    count=count+1
                    fa.write('\t' + parse.unquote(line[:len(line) - 1],'utf-8') + '\t' + str(r["intentPredictions"][0]["name"]) + '\n')
                    for dic in listdic:
                        if dic['name']==l:
                            dic['false']['negative'] += 1
                        else:
                            dic['false']['positive'] += 1
a=[]
b=[]
e=[]
g=[]
#print(r.json())
for dic in listdic:
   a.append(dic['true']['positive']/(dic['false']['positive']+dic['true']['positive']))
'''for dic in listdic:
   d.append(dic['true']['positive']/(dic['true']['positive']+dic['false']['negative']))
'''
for dic in listdic:
   g.append(((dic['true']['positive']+dic['true']['negative'])/(dic['true']['positive']+dic['true']['negative']+dic['false']['positive']+dic['false']['negative'])))
for dic in listdic:
   b.append(dic['true']['positive']/(dic['true']['positive']+dic['false']['negative']))
for (c,d) in zip(a,b):
    if c==0 and d==0:
        pass
    else:
        e.append((2*c*d)/(c+d))
print('new line count is '+str(count))
print(a)
print(b)
print(e)
print(g)
fa.close()
print('error count is ')
print(countoferrors)
