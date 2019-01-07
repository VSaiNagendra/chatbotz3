import requests
from urllib import parse

countoferrors=0
ssdic={'name':'salaryslip','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
srdic={'name':'salaryrelease','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
sbdic={'name':'salarybreakup' ,'true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
itdic={'name':'itform', 'true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
fdic={'name':'form16','true':{'positive':0,'negative':0},'false':{'positive':0,'negative':0}}
filenames=['form16','itform','salarybreakup','salaryrelease','salaryslip']
listdic=[fdic,itdic,sbdic,srdic,ssdic]
foh=open('heuristics.txt','w+')
r={}
for l in filenames:
    foh.write('\n----------------'+l+'---------------------\n')
    with open('{0}test'.format(l),'r+') as fread:
            for line in fread.readlines():
                if line=='\n':
                    continue
                line = parse.quote(line)
                params = {
                    # Query parameter
                    'q': '{0}'.format(line.encode('utf-8')),
                    'model':'umodel'
                    # Optional request parameters, set to default values
                    #'subscription-Key':'7a59937e80dd423fa5415fdbd8289275',
                }
                """r = requests.get(
                    'https://westus.api.cognitive.microsoft.com/luis/webapi/v2.0/apps/087f2913-a411-4527-a031-c68948495d1d/versions/0.1/predict',
                        params=params).json()"""
                #r=requests.get('https://westus.api.cognitive.microsoft.com/luis/webapi/v2.0/apps/087f2913-a411-4527-a031-c68948495d1d/versions/0.1/predict?subscription-Key=7a59937e80dd423fa5415fdbd8289275&example={0}&patternDetails=true'.format(line))
                try:
                    r=requests.get('http://172.16.6.101:5000/parse?model=umodel&q={0}'.format(line),params=None)
                    r = r.json()
                    if not (r["topScoringIntent"]["intent"]):
                        r["topScoringIntent"]["intent"]='None'
                    if l==r["topScoringIntent"]["intent"]:
                        for dic in listdic:
                            if dic['name']==l:
                                dic['true']['positive']+=1
                            else:
                                dic['true']['negative']+=1
                    else:
                        foh.write('\t'+line[:len(line)-1]+'\t'+str(r["topScoringIntent"]["intent"])+'\n')
                        for dic in listdic:
                            if dic['name']==l:
                                dic['false']['negative'] += 1
                            else:
                                dic['false']['positive'] += 1
                except Exception as e:
                    countoferrors=countoferrors+1
                    print(line)
                    print(e.__class__)
                    print('Exception caught ')
                    continue
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
    print(dic)
for dic in listdic:
   g.append(((dic['true']['positive']+dic['true']['negative'])/(dic['true']['positive']+dic['true']['negative']+dic['false']['positive']+dic['false']['negative'])))
for dic in listdic:
   b.append(dic['true']['positive']/(dic['true']['positive']+dic['false']['negative']))
for (c,d) in zip(a,b):
    if c==0 and d==0:
        pass
    else:
        e.append((2*c*d)/(c+d))
print(a)
print(b)
print(e)
print(g)
print('count is ')
print(countoferrors)
            #conn = httplib2.HTTPSConnectionWithTimeout("westus.api.cognitive.microsoft.com")
            #line=unicode(line,"utf-8")
            #conn.request("GET", "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/573a1ae6-4fbb-40ad-b353-6a085112755c?subscription-key=3f88533f3ac04af787adaeb946f26956&spellCheck=true&bing-spell-check-subscription-key=YOUR_BING_KEY_HERE&verbose=true&timezoneOffset=-360&q={0}".format(line.encode("utf-8