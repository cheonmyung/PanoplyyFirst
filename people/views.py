from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import MyUser

from .forms import RegisterForm, LoginForm, ComRegisterForm, ComLoginForm
# Create your views here.


## Main Pages

class StudentLandingView(TemplateView):
	template_name = 'base/student_home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(StudentLandingView, self).get_context_data(*args, **kwargs)
		#context["title"] = "This is homepage for students"
		return context


class CompanyLandingView(TemplateView):
	template_name = 'base/company_home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CompanyLandingView, self).get_context_data(*args, **kwargs)
		context["title"] = "This is homepage for companies"
		return context




## Student Sign up & Log In & Logout

def student_register(request):

	form = RegisterForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		school = form.cleaned_data['school']

		#MyUser.objects.create_user(username=username, email=email, password=password)
		

		new_user = MyUser()
		#new_user = MyUser.objects.all()

		new_user.username = username
		new_user.email = email

		#user's type will be student after sign up using the RegisterForm.
		new_user.user_type = 'Student'
		new_user.school = school

		#new_user.first_name = first_name
		#new_user.last_name = last_name
		#new_user.password = password #WRONG
		new_user.set_password(password) #RIGHT

		#new_user.user_type = user_type

		new_user.save()

		#ADD MESSAGE for success.
		print username, email, password
		return redirect('/')
		#return HttpResponseRedirect(reverse('login'))
		



	# name = "Justin"
	# videos = Video.objects.all()
	# embeds = []

	# for vid in videos:
	# 	code = mark_safe(vid.embed_code)
	# 	embeds.append("%s" %(code))

	context = {
		"form": form,
		"action_value": "",
		"submit_btn_value": "Register",
		# "the_name": name,
		# "number": videos.count(),
		# "videos": videos,
		# "the_embeds": embeds,
		# "a_code": mark_safe(videos[0].embed_code)
	}
	return render(request, "students/student_register.html", context)




def student_login(request):

	login_form = LoginForm(request.POST or None)
	#next_url = request.GET.get('next')

	if login_form.is_valid():
		username_email = login_form.cleaned_data['username']
		password = login_form.cleaned_data['password']
		#print username, password
		try:
			the_user = MyUser.objects.get(username=username_email)
		except MyUser.DoesNotExist:
			the_user = MyUser.objects.get(email=username_email)
		except:
			the_user = None

			#the_user = None

		if the_user is not None:

			
			user = authenticate(username=the_user.username, password=password)

			if user.user_type == 'Student':


				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print inactive

			else:
				return HttpResponseRedirect('/company_login/')

		else:
			return HttpResponseRedirect('/student_register/')
			#return HttpResponseRedirect(next_url)

	context = {
		"login_form": login_form, 
		"action_value": "", 
		"submit_btn_value": "Log In",
	}
	return render(request, "students/student_login.html", context)




def student_logout(request):
	logout(request)
	return HttpResponseRedirect('/')







## Company Sign Up & Log In & Logout

def company_register(request):

	
	com_form = ComRegisterForm(request.POST or None)

	if com_form.is_valid():
		username = com_form.cleaned_data['username']
		email = com_form.cleaned_data['email']
		password = com_form.cleaned_data['password2']
		#MyUser.objects.create_user(username=username, email=email, password=password)
		

		com_user = MyUser()
		#new_user = MyUser.objects.all()

		com_user.username = username
		com_user.email = email

		#user's type will be student after sign up using the RegisterForm.
		com_user.user_type = 'Company'

		#new_user.first_name = first_name
		#new_user.last_name = last_name
		#new_user.password = password #WRONG
		com_user.set_password(password) #RIGHT

		#new_user.user_type = user_type

		com_user.save()

		#ADD MESSAGE for success.
		print username, email, password
		#return redirect('/company/')
		return HttpResponseRedirect('/company_login/')

		#return HttpResponseRedirect(reverse('login'))
		



	# name = "Justin"
	# videos = Video.objects.all()
	# embeds = []

	# for vid in videos:
	# 	code = mark_safe(vid.embed_code)
	# 	embeds.append("%s" %(code))

	context = {
		"com_form": com_form,
		"action_value": "",
		"submit_btn_value": "Register",
		# "the_name": name,
		# "number": videos.count(),
		# "videos": videos,
		# "the_embeds": embeds,
		# "a_code": mark_safe(videos[0].embed_code)
	}
	return render(request, "companies/company_register.html", context)





def company_login(request):

	pany_form = ComLoginForm(request.POST or None)
	#next_url = request.GET.get('next')

	if pany_form.is_valid():
		username_email = pany_form.cleaned_data['username']
		password = pany_form.cleaned_data['password']
		#print username, password
		try:
			the_company = MyUser.objects.get(username=username_email)
		except MyUser.DoesNotExist:
			the_company = MyUser.objects.get(email=username_email)
		except:
			the_company = None

			#the_user = None

		if the_company is not None:

			user = authenticate(username=the_company.username, password=password)

			if user.user_type == 'Company':

				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/company/')
				else:
					print inactive

			else:
				return HttpResponseRedirect('/student_login/')


		else:
			return HttpResponseRedirect('/company_register/')
			#return HttpResponseRedirect(next_url)

	context = {
		"pany_form": pany_form, 
		"action_value": "", 
		"submit_btn_value": "Log In",
	}
	return render(request, "companies/company_login.html", context)




def company_logout(request):
	logout(request)
	return HttpResponseRedirect('/company/')






