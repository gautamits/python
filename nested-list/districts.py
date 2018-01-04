dist = open("districts.txt","r")
text = dist.readlines()
state=""
country={}
for i in text:
	line=i.rstrip('\n')
	line=line.rstrip()
	line=line.split(" ")
	for i in range(len(line)):
		line[i]=line[i].rstrip('\t')
		line[i]=line[i].lstrip('\t')
		line[i]=line[i].strip()
	if len(line) <= 3:
		state=" ".join(line)
		if not state in country:
			country[state]=[]
		#print(state)
	else:
		#data exists
		columns=7
		data=["None"]*7
		if line[0] != line[0].upper():
			#which means district code does not exist
			columns-=1
			data[0]="None"
		else:
			data[0]=line[0]
			line=line[1:]
		if not line[-1].startswith('http'):
			#website does not exists
			columns-=1
			data[6]="None"
		else:
			data[6]=line[-1]
			line=line[:-1]
		try:
			for i in [5,4,3,2]:
				data[i]=line[-1]
				line=line[:-1]
			data[1]=" ".join(line)
			country[state].append(data)
		except:
			pass
		#print(str(dist))
		form=[5,20,15,15,10,5,30]
		for states in country:
			for v in country[states]:
				print('{:5} {:30} {:15} {:15} {:10} {:7} {:30}'.format(*[v[i] for i in range(7)]))
		
