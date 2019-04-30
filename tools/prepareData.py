#!/usr/bin/python3
# -*- coding: utf-8 -*-

# installation
# sudo pip3 install -U spacy
# sudo pip3 install jieba
# from spacy.lang.zh import Chinese
# nlp = Chinese()
# doc = nlp(u"会谈前，习近平在人民大会堂北大厅为金正恩举行欢迎仪式。")
# for t in doc: print(t.text)

# alternative
#sudo pip3 install thulac
# import thulac	
#thu1 = thulac.thulac()  #默认模式
#text = thu1.cut("我爱北京天安门", text=True)  #进行一句话分词
#print(text)


import re, copy, os, html.entities
from segtok.segmenter import split_single
from lib import conll, transconll, docopt

try:
	import tqdm
	tqdm.monitor_interval = 0
except:
	pass

import spacy
nlp_en = spacy.load('en')


def usub(m): 
	return html.entities.html5[m.group(0)[1:]]

def textCorrection(t):
	t = t.replace("&amp;","&")
	entity = re.compile(r"&\w+;")
	t = entity.sub(usub, t)
	
	return t
	


def toSentences(infile, outfile):
	"""
	simple function: just creates an html file to view a conllu file
	
	"""
	triple = re.compile(r"\s*\n\s*\n\s*\n\s*",re.M)
	double = re.compile(r"\s*\n\s*\n\s*",re.M)
	sentpunct = re.compile(r"([!?.;]+)\s*")
	
	
	text = open(infile).read()
	
	outstr = ""
	
	for sect in triple.split(text):
		
		if len(double.split(sect)) !=2:
			sqdf
		
		t = textCorrection(double.split(sect)[1])
		
		t = sentpunct.sub(r"\1 ",t)
		#print(t)
		t = "\n".join(split_single(t))
		
		outstr += t.strip()+"\n"
	
	open(outfile,"w").write(outstr)
		
	
#toSentences("levelB2sp.txt","sp.txt")
#toSentences("levelB2fr.txt","fr.txt")

#to, when, which, who, that, no
gto="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	to	_	_	_	_	8	.*	_	_
""".strip()
sgto = transconll.SearchGrammar(gto)

gwhen="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	when	_	_	_	_	8	.*	_	_
""".strip()
sgwhen = transconll.SearchGrammar(gwhen)

gwhich="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	which	_	_	_	_	8	.*	_	_
""".strip()
sgwhich = transconll.SearchGrammar(gwhich)
gwhichsubj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	which	_	_	_	_	8	nsubj	_	_
""".strip()
sgwhichsubj = transconll.SearchGrammar(gwhichsubj)


gwho="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	who	_	_	_	_	8	.*	_	_
""".strip()
sgwho = transconll.SearchGrammar(gwho)
gwhosubj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	who	_	_	_	_	8	nsubj	_	_
""".strip()
sgwhosubj = transconll.SearchGrammar(gwhosubj)
gwhoobj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	who	_	_	_	_	8	dobj	_	_
""".strip()
sgwhoobj = transconll.SearchGrammar(gwhoobj)


gthat="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	that	_	_	_	_	8	.*	_	_
""".strip()
sgthat = transconll.SearchGrammar(gthat)
gthatsubj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	that	_	_	_	_	8	nsubj	_	_
""".strip()
sgthatsubj = transconll.SearchGrammar(gthatsubj)
gthatobj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	that	_	_	_	_	8	dobj	_	_
""".strip()
sgthatobj = transconll.SearchGrammar(gthatobj)

gno="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	_	_	_	_	_	8	.*	_	_
""".strip()
sgno = transconll.SearchGrammar(gno)
gnosubj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	_	_	_	_	_	8	nsubj	_	_
""".strip()
sgnosubj = transconll.SearchGrammar(gnosubj)
gnoobj="""
7	_	_	_	_	_	0	_	_	_
8	_	_	_	_	_	7	relcl	_	_
9	_	_	_	_	_	8	dobj	_	_
""".strip()
sgnoobj = transconll.SearchGrammar(gnoobj)




conlltree="""# Do you know someone who wants to bring a complaint about discrimination and what type of discrimination?
# 7, fr, 82909, 74
1	Do	do	VBP	_	_	3	aux	_	_
2	you	-PRON-	PRP	_	_	3	nsubj	_	_
3	know	know	VB	_	_	0	ROOT	_	_
4	someone	someone	NN	_	_	3	dobj	_	_
5	who	who	WP	_	_	6	nsubj	_	_
6	wants	want	VBZ	_	_	4	relcl	_	_
7	to	to	TO	_	_	8	aux	_	_
8	bring	bring	VB	_	_	6	xcomp	_	_
9	a	a	DT	_	_	10	det	_	_
10	complaint	complaint	NN	_	_	8	dobj	_	_
11	about	about	IN	_	_	10	prep	_	_
12	discrimination	discrimination	NN	_	_	11	pobj	_	_
13	and	and	CC	_	_	12	cc	_	_
14	what	what	WDT	_	_	15	det	_	_
15	type	type	NN	_	_	12	conj	_	_
16	of	of	IN	_	_	15	prep	_	_
17	discrimination	discrimination	NN	_	_	16	pobj	_	_
18	?	?	.	_	_	3	punct	_	_
"""

def matchGrammar(sg,tree):
	matchingRoots = sg.findall(tree)
	#if matchingRoots: print("match")
	return matchingRoots


#print(matchGrammar(sg,conll.conll2tree(conlltree)))
#qsdf

def getConll(doc, code=None):
	conll = "# "+doc.text+'\n'
	if code: conll+= "# "+code+'\n'
	for i, word in enumerate(doc):
		if word.head == word:
			head_idx = 0
		else:
			head_idx = word.head.i - doc[0].i + 1
		conll+="%d\t%s\t%s\t%s\t%s\t%s\t%s\t_\t_"%(
		i+1, # There's a word.i attr that's position in *doc*
		word,
		word.lemma_,
		word.tag_, # Fine-grained tag
		'_\t_',#word.ent_type_,
		str(head_idx),
		word.dep_ # Relation
		)+"\n"
	return conll
	  

def xmlToSentences(infile):
	outfile = infile.split(".")[0]+".sentences"
	infofile = infile.split(".")[0]+".info"
	conllfile = infile.split(".")[0]+".conllu"
	resfile = infile.split(".")[0]+".tsv"
	
	sentpunct = re.compile(r"([!?.;]+)\s*")
	double = re.compile(r"\s*\n\s*\n\s*",re.M)
	multispace = re.compile(r"  +")
	
	
	
	relearnat = re.compile(r'<learner id="(\d+)" nationality="(\w+)"',re.M) #<learner id="82909" nationality="fr"/>
	retop = re.compile(r'<topic id="(\d+)">(.*)</topic>',re.M) #<topic id="74">Doing a survey about discrimination</topic>
	retext = re.compile(r'<text>(.*)</text>',re.M+re.DOTALL) #<topic id="74">Doing a survey about discrimination</topic>

	
	text = open(infile).read()
	segs = text.split("<writing ")
	
	counter = 0
	with open(outfile,"w") as outf, open(infofile,"w") as infof, open(conllfile,"w") as conllf, open(resfile,"w") as resf:
		for seg in segs:
			if '<text>' in seg:
				#print(seg)
				
				for m in relearnat.finditer(seg): learner,nationality = m.group(1), m.group(2)
				for m in retop.finditer(seg): topid, topic = m.group(1), m.group(2)
				for m in retext.finditer(seg): segtext= m.group(1).strip().replace('<br/>','\n').replace('&amp;quot;','"')
				segtext = double.sub('\n',segtext)
				segtext = multispace.sub(' ',segtext)
				
				for li in segtext.split('\n'):
					#print(4444,li)
					doc = nlp_en(li)
					for s in doc.sents:
						#print(s.text)
						outf.write(s.text+"\n")
						infof.write("\t".join([nationality,learner,topid, topic,s.text])+'\n')
						counter+=1
						conlltext = getConll(s, ", ".join([str(counter),nationality,learner,topid]))
						conllf.write(conlltext+'\n')
						tree = conll.conll2tree(conlltext)
						print("___________",s.text)
						print(tree)
						print(conlltext)
						toinds=[]
						prorelinds=[]
						#to, when, which, who, that, no
						for mat in matchGrammar(sgto,tree):
							toinds+=[mat]
							#print(mat not in prorelinds+toinds, prorelinds+toinds)
							#qsdf
						for mat in matchGrammar(sgwhen,tree):
							if mat not in toinds:
								prorelinds+=[mat]
								resf.write("\t".join([str(counter), str(mat-1), "when", "other", s[mat-1].text, s.text, topid, topic, nationality, learner])+'\n')
						for mat in matchGrammar(sgwhich,tree):
							if mat not in toinds:
								prorelinds+=[mat]
								if mat in matchGrammar(sgwhichsubj,tree): rel = "subj"
								elif mat in matchGrammar(sgwhichobj,tree): rel = "obj"
								else: rel="other"
								resf.write("\t".join([str(counter), str(mat-1), "which", rel, s[mat-1].text, s.text, topid, topic, nationality, learner])+'\n')
						for mat in matchGrammar(sgwho,tree):
							if mat not in toinds:
								prorelinds+=[mat]
								if mat in matchGrammar(sgwhosubj,tree): rel = "subj"
								elif mat in matchGrammar(sgwhoobj,tree): rel = "obj"
								else: rel="other"
								resf.write("\t".join([str(counter), str(mat-1), "who", rel, s[mat-1].text, s.text, topid, topic, nationality, learner])+'\n')
						for mat in matchGrammar(sgthat,tree):
							if mat not in toinds:
								prorelinds+=[mat]
								if mat in matchGrammar(sgthatsubj,tree): rel = "subj"
								elif mat in matchGrammar(sgthatobj,tree): rel = "obj"
								else: rel="other"
								resf.write("\t".join([str(counter), str(mat-1), "that", rel, s[mat-1].text, s.text, topid, topic, nationality, learner])+'\n')
						for mat in matchGrammar(sgno,tree):
							if mat not in prorelinds+toinds:
								if mat in matchGrammar(sgnosubj,tree): rel = "subj"
								elif mat in matchGrammar(sgnoobj,tree): rel = "obj"
								else: rel="other"
								resf.write("\t".join([str(counter), str(mat-1), "no", rel, s[mat-1].text, s.text, topid, topic, nationality, learner])+'\n')
							
						
						if not counter%1000: print(counter)
					#if counter>14: break
			#if counter>14: break
						
						
						
						
	print("wrote",counter,"sentences")
					#for sent in split_single(li):
						#print(111,sent)
				#print(topid,topic,learner,nationality,segtext)
				
				
				
				#qsdf
			
xmlToSentences("paula/FR_b2.xml")
xmlToSentences("paula/SP_b2.xml")
