#!/usr/bin/env python
import json
import re
file1=open('rule.txt','r')
file2=open('rule.json','w')
string_try=""
rules=[]
for line in file1:
	
	if line=="" or line=="\n":
		continue
	else:
		string_try+=line
	if "AND" not in line:
		
		#print string_try
		string_try=string_try.replace("\n"," ")
		occur=[m.start() for m in re.finditer('AND', string_try)]
		actor=[]
		diction={}
		for i in range (0,len(occur)):
		   W={}
		   if i==0:
		       a=(string_try[0:occur[i]].strip())
		   elif i==(len(occur)-1):
		       a=(string_try[occur[i]+3:string_try.find(':')].strip())
		   else:
		       a=(string_try[occur[i]+3:occur[i+1]].strip())
		   W['key']=unicode(a[0:a.find('=')].strip(),errors='replace')
		   W['value']=a[a.find('=')+1:].strip()
		   actor.append(W)
		diction['X']=actor
		string_try1=string_try[string_try.find(':')+1:]
		Y=string_try1[0:string_try1.find('(')].strip()
		if Y=='one':

			diction['Y']="Rating 1"
		elif Y=='two':
			diction['Y']="Rating 2"
		elif Y=='three':
			diction['Y']="Rating 3"
		elif Y=='four':
			diction['Y']="Rating 4"
		elif Y=='five':
			diction['Y']="Rating 5"
		elif Y=='six':
			diction['Y']="Rating 6"
		elif Y=='seven':
			diction['Y']="Rating 7"
		elif Y=='eight':
			diction['Y']="Rating 8"
		elif Y=='nine':
			diction['Y']="Rating 9"
		elif Y=='ten':
			diction['Y']="Rating 10"
		
		subs=string_try[string_try.find("(")+1:string_try.find(")")].strip()
		coverage=0
		accuracy=0
		if "/" in subs:
			coverage=float(subs[:subs.find("/")].strip())+float(subs[subs.find("/")+1:].strip())
			accuracy=(float(subs[:subs.find("/")].strip())*100)/(float(subs[:subs.find("/")].strip())+float(subs[subs.find("/")+1:].strip()))
		else:
			coverage=float(subs[:subs.find(")")].strip())
			accuracy=100
		
		diction["coverage"]=coverage
		diction["accuracy"]=accuracy
		rules.append(diction)
		string_try=""
json.dump(rules, file2)		
		