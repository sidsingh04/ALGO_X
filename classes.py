# used for fcfs,sjf,srtf,hrrn,round-robin
class Process1:
	def __init__(self,a,b,c):
		self.pid=a
		self.at=b
		self.bt=c
		self.ct=-1
		self.rt=c
		self.tat=-1
		self.wt=-1
		self.isReady=False

# for Pre-Priority and Non-Premptive Priority
class Process2:
	def __init__(self,a,b,c,d):
		self.pid=a
		self.at=b
		self.bt=c
		self.priority=d
		self.ct=-1
		self.rt=c
		self.tat=-1
		self.wt=-1
		self.isReady=False


class GanttChart:
	def __init__(self):
		self.cap=0
		self.Chart=[]

	def push(self,row):
		self.Chart.append(row)
		self.cap=self.cap+1

class GanttRow:
	def __init__(self,pid,st,et):
		self.pid=pid
		self.st=st
		self.et=et
