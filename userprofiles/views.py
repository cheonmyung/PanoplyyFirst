from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from people.models import MyUser
#from django.views.generic.list import ListView

MyUser = get_user_model()

from .models import Profile
from .forms import ProfileForm
from projects.models import Project, ProjectLike
from trys.models import BookMarks



## Student profile

#class StudentListView(ListView):
#	model = MyUser
#	template_name = 'students/student_profile.html'



@login_required
def profile_user(request):

	student = MyUser.objects.student_type()
	if student:
		user = get_object_or_404(MyUser, username=request.user)
		profile, created = Profile.objects.get_or_create(user=user)
		context = {
			"profile": profile,
								}
		return render(request, "students/student_user.html", context)
	else:
		user = get_object_or_404(MyUser, username=request.user)
		profile, created = Profile.objects.get_or_create(user=user)
		context = {
			"profile": profile,
								}
		return render(request, "companies/company_user.html", context)



@login_required
def profile_edit(request):

	title = "Update Profile"
	profile, created = Profile.objects.get_or_create(user=request.user)
	form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("profile_view", username=instance.user.username)
	context = {
		"form": form,
		"title": title,
				}
	return render(request, "students/forms.html", context)





@login_required
def profile_view(request, username):
		user = get_object_or_404(MyUser, username=username)
		profile, created = Profile.objects.get_or_create(user=user)

		
		#items = Project.objects.filter(user_student=request.user)

		#items = Project.objects.get(slug=slug)
		#p = Picture.objects.get(...)
		#number_of_likes = p.like_set.all().count()

		if user.user_type == 'Student':

			user = ProjectLike.objects.get(user=request.user)
			#items = user.liked_projects.all()
			items = user.liked_projects.only_active()

			#items = ProjectLike.objects.filter(user=request.user)
			#items = Project.objects.filter(user_student=request.user)

			# if use Post_save signals from ProjectLike,
			# items = Project.objects.filter(user_student=request.user)

			#items = Project.objects.all()
			#hello = ProjectLike.objects.all()
			#projects = Project.objects.all()
			#if hello == request.user:
			#	if projects in hello.liked_projects.all():
				#if projects in request.user.projectlike.liked_projects.all():
			#		projects.user_student = request.user
			#		projects.save()
			#		if projects:
						#			return items

			#user_like, user_like_created = ProjectLike.objects.get_or_create(user=request.user)
			#do_i_like = False
			#if items in user_like.liked_projects.all():
			#	items.user_student == request.user
			#	items.save()
				#do_i_save = True
				#if project.user_student == request.user:
				#	items = Project.objects.filter(user_student=request.user)
				


			#items = Project.objects.filter(user_student=request.user)

			#items = ProjectLike.objects.filter(user=request.user)


			#user = ProjectLike.objects.filter(user=request.user)
			#items = user.liked_projects.all()

				

			#do_i_save = False
			#if items in request.user.projectlike.liked_projects.all():
			#	do_i_save = True

			#pending_like = get_object_or_404(Project, slug=slug)
			#project = get_object_or_404(Project, id=id)
			
			#user_like, created = ProjectLike.objects.get_or_create(user=request.user)
			#if created:
			#	projects = user_like.liked_projects.all()
			
			#if pending_like in user_like.liked_projects.all():
			#		user_like.liked_projects.remove(pending_like)
			#else:
			#		user_like.liked_projects.add(pending_like)

			#projects = Project.objects.all()

			#student = ProjectLike.objects.filter(user=request.user)
			#projects = student.liked_projects.all()

			#projects = ProjectLike.objects.filter(user=request.user)

			#projects = Project.objects.get(user_student=request.user)

			
			#p = ProjectLike.objects.get(user=request.user) # filter or get ??
			#projects = p.liked_projects.all()

			#student_like, student_like_created = ProjectLike.objects.get_or_create(user=request.user)
			#do_i_save = False
			#if project in student_like.liked_projects.all():
				#do_i_save = True
			context = {
				"profile": profile,
				#"projects": projects,
				"items": items,
				#"do_i_save": do_i_save,
				#"hello": hello,
			}

			return render(request, "students/student_profile.html", context)
		else:
			posts = Project.objects.filter(user_company=request.user)
			context = {
				"profile": profile,
				"posts": posts,
			}

			return render(request, "companies/company_profile.html", context)
			









			#project = Project()
			#if project.user_company == request.user
			#project = Project.objects.get(user_company=request.user)
			#if project:
			#	try:
			#	posts = Project.objects.only_active()
			#	except 
			#context = {
			#	"profile": profile,
			#	"posts": posts,
			#}
			


		#project = Project()
		#if project.user_company == 		
		#posts = Project.objects.only_active(request.user)
		#context = {"profile": profile, "posts": posts}
		#if user.user_type == 'Student':
		#	return render(request, "students/student_profile.html", context)
		#else:
		#	return render(request, "companies/company_profile.html", context)




#@login_required
#def profile_view(request, username):
#	user = get_object_or_404(User, username=username)
#	profile, created = Profile.objects.get_or_create(user=user)


#	user_like, user_like_created = UserLike.objects.get_or_create(user=request.user)
#	do_i_like = False
#	if user in user_like.liked_users.all():
#		do_i_like = True
#	mutual_like = user_like.get_mutual_like(user)
#	match, match_created = Match.objects.get_or_create_match(user_a=request.user, user_b=user)
#	jobs = user.userjob_set.all()
#	context = {
#		"profile": profile,
#		"match": match,
#		"jobs": jobs,
#		"mutual_like": mutual_like,
#		"do_i_like": do_i_like
#				}
#	return render(request, "profiles/profile_view.html", context)