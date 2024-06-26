from classes import Process1,Process2,GanttChart,GanttRow

cur_time=-1
# function for sorting processes on the basis of their arrival time and pid
def sort(process):
	newPro=sorted(process,key=lambda x:(x.at,x.pid))
	return newPro

# function to sort on basis of BT,AT,PID
def sortBT(process):
	newPro=sorted(process,key=lambda x:(x.bt,x.at,x.pid))
	return newPro

# function to sort on basis of Response Ratio in decreasing order
def sortRR(process):
	newPro=sorted(process,key=lambda x:((cur_time-x.at+x.bt)/x.bt,x.pid),reverse=True)
	return newPro

def sortPri(process):
	newPro=sorted(process,key=lambda x:(x.priority,x.pid),reverse=True)
	return newPro

def sortRT(process):
	newPro=sorted(process,key=lambda x:(x.rt,x.pid))
	return newPro


# function to calculate tat and wt of every process
def generateParams(process):
	for p in process:
		p.tat=p.ct-p.at
		p.wt=p.tat-p.bt
	return process


def FCFS(process):
	newPro=sort(process)
	GChart=GanttChart()
	time=newPro[0].at
	for execution in newPro:
		temp=time
		execution.isReady=True
		execution.ct=time+execution.bt
		time=time+execution.bt
		row=GanttRow(execution.pid,temp,time)
		GChart.push(row)
		execution.isReady=False
		execution.rt=0

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0
	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt
	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(GChart)

	return res_list



def SJF(process):
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	ready=[]
	compList=[]
	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	ready=sortBT(ready)
    # ensure that changes are migrated to the newPro from Ready queue
	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		time=time+execution.bt
		newPro[index].ct=time
		newPro[index].rt=0
		newPro[index].isReady=False
		Gchart.push(GanttRow(execution.pid,temp,time))
		
		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt>0:
				ready.append(p)
				p.isReady=True

		ready=sortBT(ready)

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list


def HRRN(process):
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	cur_time=time
	ready=[]
	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	ready=sortRR(ready)

	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		time=time+execution.bt
		newPro[index].ct=time
		newPro[index].rt=0
		newPro[index].isReady=False
		Gchart.push(GanttRow(execution.pid,temp,time))
		cur_time=time

		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt!=0:
				ready.append(p)
				p.isReady=True

		ready=sortRR(ready)

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list


def Non_Pre_Priority(process):
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	ready=[]
	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	ready=sortPri(ready)

	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		time=time+execution.bt
		newPro[index].ct=time
		newPro[index].rt=0
		newPro[index].isReady=False
		Gchart.push(GanttRow(execution.pid,temp,time))

		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt!=0:
				ready.append(p)
				p.isReady=True

		ready=sortPri(ready)

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list



def Pre_Priority(process):
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	ready=[]
	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	ready=sortPri(ready)

	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		time=time+1
		newPro[index].rt=newPro[index].rt-1
		if newPro[index].rt==0:
			newPro[index].ct=time
			newPro[index].isReady=False
		else:
			ready.append(newPro[index])

		Gchart.push(GanttRow(execution.pid,temp,time))

		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt!=0:
				ready.append(p)
				p.isReady=True

		ready=sortPri(ready)

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list



def Round_Robin(process,tq):	
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	ready=[]
	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		if execution.rt<=tq:
			time=time+execution.rt
			newPro[index].ct=time
			newPro[index].rt=0
			newPro[index].isReady=False
		else:
			time=time+tq
			newPro[index].rt=newPro[index].rt-tq

		Gchart.push(GanttRow(execution.pid,temp,time))

		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt!=0:
				ready.append(p)
				p.isReady=True

		if newPro[index].rt!=0:
			ready.append(newPro[index])

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list


def SRTF(process):
	newPro=sort(process)
	Gchart=GanttChart()
	time=newPro[0].at
	ready=[]

	for p in newPro:
		if p.at==time:
			ready.append(p)
			p.isReady=True

	ready=sortRT(ready)

	while len(ready)!=0:
		execution=ready[0]
		index=newPro.index(execution)
		ready=ready[1:]
		temp=time
		time=time+1
		newPro[index].rt=newPro[index].rt-1
		if newPro[index].rt==0:
			newPro[index].ct=time
			newPro[index].isReady=False
		else:
			ready.append(newPro[index])

		Gchart.push(GanttRow(execution.pid,temp,time))

		for p in newPro:
			if p.at<=time and p.isReady==False and p.rt!=0:
				ready.append(p)
				p.isReady=True

		ready=sortRT(ready)

	schedule_len=time-newPro[0].at
	res_list=generateParams(newPro)
	tat=0
	wt=0

	for i in res_list:
		tat=tat+i.tat
		wt=wt+i.wt

	tat=tat/len(process)
	wt=wt/len(process)

	res_list.append(tat)
	res_list.append(wt)
	res_list.append(schedule_len)
	res_list.append(Gchart)

	return res_list



    