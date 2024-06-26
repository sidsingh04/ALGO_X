from flask import Flask,render_template,request,redirect,flash
from validate import validate1,validate2,validate3,package1,package2,package3
from classes import Process1,Process2
from algo import FCFS,SJF,HRRN,SRTF,Non_Pre_Priority,Pre_Priority,Round_Robin

app=Flask(__name__,template_folder="template")
app.secret_key="price"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/fcfs",methods=["GET","POST"])
def land1():
	if request.method=='GET':
		return render_template("fcfs.html",title="FCFS",link="/fcfs")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate1(li)

		if valstr=='correct':
			if package1(li)==1:
				flash("Pid of every process must be unique")
				return redirect("fcfs")
			Process=package1(li)
			Res=FCFS(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			# attr1=Res[slice_index:len(Res)]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]
			
			return render_template("outfcfs.html",title="FCFS",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)

		else:
			flash(valstr)
			return redirect("fcfs")


		

@app.route("/sjf",methods=["GET","POST"])
def land2():
	if request.method=='GET':
		return render_template("sjf.html",title="SJF",link="/sjf")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate1(li)

		if valstr=='correct':
			if package1(li)==1:
				flash("Pid of every process must be unique")
				return redirect("sjf")
			Process=package1(li)
			Res=SJF(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outsjf.html",title="SJF",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)
		else:
			flash(valstr)
			return redirect("sjf")

@app.route("/round-robin",methods=["GET","POST"])
def land3():
	if request.method=='GET':
		return render_template("round.html",title="ROUND-ROBIN",link="/round-robin")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate3(li)

		if valstr=='correct':
			if package3(li)==1:
				flash("Pid of every process must be unique")
				return redirect("round-robin")
			Process=package3(li)
			tq=Process[0]
			Process=Process[1:]
			Res=Round_Robin(Process,tq)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outrr.html",title="ROUND-ROBIN",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)
		else:
			flash(valstr)
			return redirect("round-robin")

@app.route("/srtf",methods=["GET","POST"])
def land4():
	if request.method=='GET':
		return render_template("srtf.html",title="SRTF",link="/srtf")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate1(li)

		if valstr=='correct':
			if package1(li)==1:
				flash("Pid of every process must be unique")
				return redirect("srtf")
			Process=package1(li)
			Res=SRTF(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outsrtf.html",title="SRTF",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)
		else:
			flash(valstr)
			return redirect("srtf")

@app.route("/hrrn",methods=["GET","POST"])
def land5():
	if request.method=='GET':
		return render_template("hrrn.html",title="HRRN",link="/hrrn")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate1(li)

		if valstr=='correct':
			if package1(li)==1:
				flash("Pid of every process must be unique")
				return redirect("hrrn")
			Process=package1(li)
			Res=HRRN(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outhrrn.html",title="HRRN",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)

		else:
			flash(valstr)
			return redirect("hrrn")

@app.route("/non-pre-priority",methods=["GET","POST"])
def land6():
	if request.method=='GET':
		return render_template("non-pre-pri.html",title="NON-PREMPTIVE-PRIORITY",link="/non-pre-priority")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate2(li)

		if valstr=='correct':
			if package2(li)==1:
				flash("Pid of every process must be unique")
				return redirect("non-pre-priority")
			Process=package2(li)
			Res=Non_Pre_Priority(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outnpr.html",title="NON-PREMPTIVE-PRIORITY",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)


		else:
			flash(valstr)
			return redirect("non-pre-priority")

@app.route("/pre-priority",methods=["GET","POST"])
def land7():
	if request.method=='GET':
		return render_template("pre-pri.html",title="PREMPTIVE-PRIORITY",link="/pre-priority")
	elif request.method=='POST':
		inputstr=request.form.get("input")
		inputstr=inputstr.strip()
		inputs=inputstr.split("\n")
		li=[]
		for x in inputs:
			x=x.strip()
			li.append(x)

		valstr=validate2(li)

		if valstr=='correct':
			if package2(li)==1:
				flash("Pid of every process must be unique")
				return redirect("pre-priority")
			Process=package2(li)
			Res=Pre_Priority(Process)
			slice_index=len(Res)-3
			res_process=Res[:slice_index]
			attr1=[Res[-4],Res[-3],Res[-2]]
			attr2=Res[-1]

			return render_template("outppr.html",title="PREMPTIVE-PRIORITY",input=Process,num=len(Process),process=res_process,param=attr1,gantt=attr2)

		else:
			flash(valstr)
			return redirect("pre-priority")



if __name__=="__main__":
	app.run(debug=True)