from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import user,content 
import time

from mywiki.forms import login_form , signup_form
# Create your views here.
def index(request):
	return render(request,'homepage.html')

def login_view(request):
	if(request.method == "POST") :
		useremail = request.POST['Email']	
		userpassword = request.POST['Password']
		if user.objects.filter(userEmail=useremail, userPassword=userpassword).exists() :
			userdataid = user.objects.all().filter(userEmail=useremail,userPassword=userpassword)
			for userid in userdataid:
				takeuserid = userid.id
				contentdata = content.objects.all().filter(userId_id=takeuserid)							 
			return render(request,'wikipage.html',{'data':takeuserid, 'contentdata':contentdata})
		else :
			return render(request,'PageNotfound.html')

	return render(request,'login.html')
			

def signup_view(request):
	if(request.method == "POST") :
		username = request.POST['Name']
		useremail = request.POST['Email']
		userpassword = request.POST['Password']
		data = user(userName = username , userEmail = useremail , userPassword = userpassword)
		data.save()
		userdataid = user.objects.all().filter(userEmail = useremail , userPassword=userpassword)
		for userid in userdataid:
			takeuserid = userid.id
			contentdata = content.objects.all().filter(userId_id=takeuserid)
		return render(request,'wikipage.html',{'data':takeuserid , 'contentdata':contentdata})
		
	return render(request,'signUp.html')

def wiki_view(request):
	Userid=0
	if(request.method == "POST"):
		text = request.POST['datacontent']
		text_title = request.POST['content_title']
		Userid = request.POST['userid'] 
   		data = content(contentTitle = text_title,content_text=text,date_added=time.strftime("%Y-%m-%d %H:%M:%S"),userId_id=Userid)	
		data.save()
		userdataid = user.objects.all().filter(id = Userid)
		for userid in userdataid:
			takeuserid = userid.id
			contentdata = content.objects.all().filter(userId_id=takeuserid)
		return render(request,'wikipage.html',{'data':Userid,'contentdata':contentdata})

	return render(request, 'wikipage.html',{'data':Userid})

def home_page(request):
	if(request.method == "POST"):
		search_text = request.POST['search']
		searchdata = content.objects.all().filter(contentTitle__contains=search_text)
		return render(request,'homepage.html',{'searchdata':searchdata})
	return render(request,'homepage.html')

def delete_content(request, id, userid):
	content_id = id
	userdataId = userid
	data = content.objects.get(id = content_id, userId_id = userdataId)
	data.delete()
	userdataid = user.objects.all().filter(id = userdataId)
	for userdata in userdataid:
		takeuserid = userdata.id
		contentdata = content.objects.all().filter(userId_id=takeuserid)
	return render(request,'wikipage.html',{'data':userdataId,'contentdata':contentdata})

def edit_content(request, id, userid):
	content_id  = id
	userdataid = userid
	data = content.objects.all().filter(id=content_id, userId_id = userdataid)
	return render(request, 'update.html', {'data':data})

def update_content(request):
	if(request.method == "POST"):
		contentText = request.POST['datacontent']
		content_title = request.POST['content_title']
		userid  = request.POST['userid']
		contentid = request.POST['contentid']
		data = content.objects.filter(id=contentid, userId_id=userid).update(contentTitle=content_title,content_text=contentText)
		datadisplay = content.objects.all().filter(userId_id=userid)
		return render(request,'wikipage.html',{'data':userid,'contentdata':datadisplay})
	return render(request,'pagenotfound.html')
	

