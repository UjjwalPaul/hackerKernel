from django.shortcuts import render , HttpResponse, redirect
from myApp. models import UserDetails,UserTask

def home(req):
	return render(req,"index.html")

def addUser(req):
	return render(req,"addUser.html")

def submitUserData(req):
	if req.method=='POST':
		print(req.POST)
		name = req.POST.get('name')
		email = req.POST.get('email')
		mobile = req.POST.get('mobile')

		data = UserDetails(name=name, email=email, mobile=mobile)
		data.save()
		return render(req, "addUser.html")
        
def addTask(req):
	return render (req,"addTask.html")

def submitTaskData(req):
	if req.method=='POST':
		print(req.POST)
		email = req.POST.get('email')
		pending = req.POST.get('pending')
		taskdetails = req.POST.get('taskdetails')

		data = UserTask(pending=pending, email=email, taskdetails=taskdetails)
		data.save()
		return HttpResponse("Sucessfully")
	

	
def userManager(req):
	if req.method=='GET':
		data = UserDetails.objects.all()
		return render(req,"Display.html", {'data':data})
	

def taskManager(req):
	if req.method=='GET':
		data = UserTask.objects.all()
		return render(req,"Displaytask.html", {'data':data})

def delete_user(req,id):
	data=UserDetails.objects.get(id=id)
	data.delete()
	return redirect('../')

def delete_task(req,id):
	data=UserTask.objects.get(id=id)
	data.delete()
	return redirect('../')