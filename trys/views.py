from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect 

# Create your views here.
from projects.models import Project, ProjectLike

#from .models import ProjectLike

MyUser = get_user_model()


def like_user(request, slug):
	pending_like = get_object_or_404(Project, slug=slug)
	#project = get_object_or_404(Project, id=id)
	user_like, created = ProjectLike.objects.get_or_create(user=request.user)
	if pending_like in user_like.liked_projects.all():
			user_like.liked_projects.remove(pending_like)
	else:
			user_like.liked_projects.add(pending_like)
	return redirect("detail", slug=pending_like.slug)



#def bookmarks_per_user(request):

	#student_like, student_like_created = ProjectLike(or BookMarks).objects.get_or_create(user=request.user)
			#do_i_save = False
			#if project in student_like.liked_projects.all():
				#do_i_save = True




#	pro = get_object_or_404(ProjectLike, user=request.user)
#	projects = pro.bookmarks_set.filter(project=request.user.liked_projects)


	#pro = get_object_or_404(Project, slug=slug)
	#projects = pro.bookmarks_set.filter(project_like_user=request.user)



#	context = {
#				"projects": projects,
				#"do_i_save": do_i_save,
#			}

#	return render(request, "students/student_profile.html", context)
