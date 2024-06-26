from classes import Process1,Process2 
# for validation of input of FCFS,SJF,HRRN,SRTF
def validate1(li):
	y=li[0].split()
	if len(y)!=1:
		return "Error in first line"
	if li[0].isdigit()==False:
		return "Only integers should be passed as input"
	n=int(li[0])
	if len(li)!=n+1:
		return "Inputs given to the program are not equal to the expected value"    
	for i in range(1,len(li)):
		x=li[i].split()
		if len(x)!=3:
			return "Process should contain only 3 attributes as input"
		for num in x:
			if num.isdigit()==False:
				return "Only integers should be passed as input"
			if int(num)<0:
				return "The input values must be non-negative integer"
	return "correct"

# for validation of PRE-PRIORITY,PRIORITY
def validate2(li):
	y=li[0].split()
	if len(y)!=1:
		return "Error in first line"
	if li[0].isdigit()==False:
		return "Only integers should be passed as input"
	n=int(li[0])
	if len(li)!=n+1:
		return "Inputs given to the program are not equal to the expected value"
	for i in range(1,len(li)):
		x=li[i].split()
		if len(x)!=4:
			return "Process should contain only 4 attributes as input"
		for num in x:
			if num.isdigit()==False:
				return "Only integers should be passed as input"
			if(int(num)<0):
				return "The input values must be non-negative integer"
	return "correct"

#for validation of Round-Robin
def validate3(li):
	y=li[0].split()    
	if(len(y)!=2):
		return "Error in first line"
	if y[0].isdigit()==False or y[1].isdigit()==False:
		return "Only integers should be passed as input"
	if int(y[0])<=0 or int(y[1])<=0:
		return "Input values in first line must be positive(>0)"
	if len(li)!=int(y[0])+1:
		return "No. of Inputs not equal to the expected value"
	for i in range(1,len(li)):
		x=li[i].split()
		if len(x)!=3:
			return "Process should contain only 3 attributes as input"
		for num in x:
			if num.isdigit()==False:
				return "Only integers should be passed as input"
			if(int(num)<0):
				return "The input values must be non-negative integer"
	return "correct"


def package1(li):
	process=[]
	num=int(li[0])
	pidset={-1}
	for i in range(1,num+1):
		x=li[i].split()
		process.append(Process1(int(x[0]),int(x[1]),int(x[2])))
		pidset.add(int(x[0]))

	if len(pidset)!=num+1:
		return 1

	return process

def package2(li):
	process=[]
	num=int(li[0])
	pidset={-1}
	for i in range(1,num+1):
		x=li[i].split()
		process.append(Process2(int(x[0]),int(x[1]),int(x[2]),int(x[3])))
		pidset.add(int(x[0]))

	if len(pidset)!=num+1:
		return 1

	return process

def package3(li):
	process=[]
	y=li[0].split()
	num=int(y[0])
	tq=int(y[1])
	process.append(tq)
	pidset={-1}
	for i in range(1,num+1):
		x=li[i].split()
		process.append(Process1(int(x[0]),int(x[1]),int(x[2])))
		pidset.add(int(x[0]))

	if len(pidset)!=num+1:
		return 1
		
	return process