#!/usr/bin/env python
import json
import csv
import re
file1=open('rule.json','r')
file2=open('rule_final.json','w')
row_count = sum(1 for row in csv.reader( open('weka_sorted.csv') ) )-1
ratings=[]
for line in file1:
	json_1=json.loads(line)
	
	for x in json_1:
		if(len(ratings)==0):
			dict_1={}
			dict_1['name']=x['Y']
			random_arr=[]
			diction={}
			diction['name']="Rules"
			rules=[]
			rule_dict={}
			rule_dict['name']="Rule 1"
			rule_dict['coverage']=x['coverage']*100/row_count
			rule_dict['accuracy']=x['accuracy']
			rule_dict['length']=len(x['X'])
			lhs=x['X']
			for z in lhs:
				z['name']=z['key'].replace("_"," ")
				z['size']=5
				
				z.pop('key',None)
			rule_dict['children']=lhs
			rules.append(rule_dict)
			diction['children']=rules
			random_arr.append(diction)
			dict_1['children']=random_arr
			ratings.append(dict_1)
		else:
			flag=0
			for y in ratings:
				if x['Y'] == y['name']:
					count=len(y['children'][0]['children'])+1
					flag=1
					rule_dict['name']="Rule "+str(count)
					rule_dict['coverage']=x['coverage']*100/row_count
					rule_dict['accuracy']=x['accuracy']
					rule_dict['length']=len(x['X'])
					lhs=x['X']
					for z in lhs:
						z['name']=z['key'].replace("_"," ")
						z['size']=5
						
						z.pop('key',None)
					rule_dict['children']=lhs
					y['children'][0]['children'].append(rule_dict)
					break
			if flag==0:
				dict_1={}
				dict_1['name']=x['Y']
				random_arr=[]
				diction={}
				diction['name']="Rules"
				rules=[]
				rule_dict={}
				rule_dict['name']="Rule 1"
				rule_dict['coverage']=x['coverage']*100/row_count
				rule_dict['accuracy']=x['accuracy']
				rule_dict['length']=len(x['X'])
				lhs=x['X']
				for z in lhs:
					z['name']=z['key'].replace("_"," ")
					z['size']=5
					z.pop('key',None)
					
				rule_dict['children']=lhs
				rules.append(rule_dict)
				diction['children']=rules
				random_arr.append(diction)
				dict_1['children']=random_arr
				ratings.append(dict_1)
json.dump(ratings, file2)		
