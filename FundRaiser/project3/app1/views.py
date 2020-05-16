from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app1.forms import JoinForm, LoginForm, DonateForm
from app1.models import Donate, OrganizationName, UserProfileCore
from django.db.models import Sum
from app1.serializers import DonateSerializer, UserSerializer, OrganizationNameSerializer 
from django.views.generic import View


class DonateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
		queryset = OrganizationName.objects.all()
		serializer_class = OrganizationNameSerializer
		permission_classes = [permissions.IsAuthenticated]

#from core.models import UserProfileCore
# Create your views here.
def home(request):
	return render(request, 'app1/home.html')


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            print(join_form.errors)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'app1/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        print(request.POST)
        # First get the username and password supplied
        username = request.POST["username"]
        password = request.POST["password"]
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
		# If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to homepage
                return redirect("/donate")
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
	
    else:
        #Nothing has been provided for username or password.
        return render(request, 'app1/login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")

def about(request):
	if not request.user.is_authenticated:
		return render(request, 'app1/login.html')
	else:
		return render(request, 'app1/about.html')

def who(request):
		#if (request.method == 'POST'):
	return render(request, 'app1/who.html' )

def donate(request):
	if not request.user.is_authenticated:
		return render(request, 'app1/login.html')
	else:
		if (request.method == 'POST'):
			form = DonateForm(request.POST);
			if (form.is_valid()):
				#user=user.request
				Wish = form.cleaned_data['Wish']  #names on the left are from form
				#Category = form.cleaned_data['Category']           #bracket names are same as left
				orgName=OrganizationName.objects.filter(id=request.POST["OrgName"]).get()	
				amount=form.cleaned_data['Amount']
				Donate(user=request.user,wish=Wish, orgName=orgName, amount=amount).save()   #first para on the left are from model
				
				tasks_obj = Donate.objects.select_related().filter(user=request.user)
				
				return render(request, 'app1/payment.html', {"alldonations": tasks_obj} )

		return render(request,'app1/donate.html',{"taskform":DonateForm})

def history(request):
	if not request.user.is_authenticated:
		return render(request, 'app1/login.html')
	else:
		if request.method == 'POST':
			t_form = DonateForm(request.POST)
			if(t_form.is_valid()):
				task_list_data = Donate.objects.get(id=t_form.cleaned_data["Ids"])
				latest_date=task_list_data.latest('date')
				#task_list_data.category =OrganizationName.objects.filter(id=request.POST["Category"]).get()						
				task_list_data.save()
				
		tasks_obj = Donate.objects.select_related().filter(user=request.user)
		return render(request, 'app1/history.html', {"alldonations": tasks_obj})

def user_profile(request):
	return render(request, 'app1/home.html')


def dashboard(request):
	task_list=Donate.objects.select_related()
	count= User.objects.all().count()
	donations=Donate.objects.all().count()
	raised=30000
	donated =task_list.aggregate(Sum('amount'))
	needed = raised - donated['amount__sum']
	return render(request,'app1/dashboard.html',{'task_list':task_list,'raised':raised,'donated':donated['amount__sum'],'count':count,'donations':donations,'needed':needed})

def profileshow(request):
	model = UserProfileCore.objects.select_related().filter(user=request.user)
	return render(request,'app1/profile.html',{'model':model})

def payment(request):
	return render(request,'app1/payment.html')