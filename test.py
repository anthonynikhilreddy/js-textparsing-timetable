import re
f=open('file.txt', 'r')
i=1
l=[]
k=0
for _ in f.read().split():
	if(i<=62):
		i=i+1
		continue
	l.append(_)
	i=i+1
mon=l[:l.index("TUE")]
tue=l[l.index("TUE"):l.index("WED")]
wed=l[l.index("WED"):l.index("THU")]
thu=l[l.index("THU"):l.index("FRI")]
fri=l[l.index("FRI"):l.index("SAT")]
fl=open('file2.txt', 'w+')
for i in tue:
	if(k==16):
		k=k+1
		fl.write("cut\n")
		continue
	if(i=="TUE"):
		fl.write(i+"\n")
	elif(i=="Theory" or i=="Lab" or i=="-" or i=="Lunch"):
		fl.write("f\n")
		k=k+1
		continue
	elif(re.search(r'([\w]+[\W])',i)):
		t=i.split('-')
		s=t[0]+"-"+t[1]+"-"+t[3]+"\n"
		fl.write(s)
	else:
		s="free\n"
		fl.write(s)
	k=k+1