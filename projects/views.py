from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project, ProjectLike

#from trys.models import ProjectLike


MyUser = get_user_model()



class MultipleObjectMixin(object):
	def get_object(self, queryset=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		if slug:
			try:
				obj = self.model.objects.get(slug=slug)
			except self.model.MultipleObjectsReturned:
				obj = self.get_queryset().first()
			except:
				raise Http404
			return obj
		raise Http404



class ProjectListView(MultipleObjectMixin, ListView):
    model = Project
    template_name = 'projects/projects.html'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):

		object_list = Project.objects.only_thirty_days()
		context = super(ProjectListView, self).get_context_data(*args, **kwargs)
		context["object_list"] = object_list
		context["now"] = timezone.now()
		return context


#class ProjectDetailView(MultipleObjectMixin, DetailView):
#	model = Project



#	def get_context_data(self, *args, **kwargs):
#
#		context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
		#if self.request.user.is_authenticated():
#		user = MyUser.objects.student_type()
		#project = Project.objects.get(id=id)
#		user_like, created = ProjectLike.objects.get_or_create()
#		do_i_like = False
#		if user == request.user:
#			if user in user_like.liked_users.all():
#				do_i_like = True
#				context["do_i_like"] = do_i_like
#				return context




def detail(request, slug):
	#project = get_object_or_404(Project, slug=slug)
	project, created = Project.objects.get_or_create(slug=slug)

	if request.user.is_authenticated():

		user_like, user_like_created = ProjectLike.objects.get_or_create(user=request.user)
		do_i_like = False
		if project in user_like.liked_projects.all():
			do_i_like = True
		context = {
			"do_i_like": do_i_like,
			"project": project,
					}
		return render(request, "projects/project_detail.html", context)
	else:
		context = {
			"project": project,
				}
		return render(request, "projects/project_detail.html", context)




	#if request.user.is_authenticated() and user.user_type == 'Student':

	#	user_like, user_like_created = ProjectLike.objects.get_or_create(user=request.user)
	#	do_i_save = False
	#	if project in user_like.liked_projects.all():
	#		do_i_save = True
	#	context = {
	#		"do_i_save": do_i_save,
	#		"project": project,
	#				}
	#	return render(request, "students/student_profile.html", context)


#def new_detail



	

#@login_required
#def profile_view(request, username):
#	user = get_object_or_404(User, username=username)
#	profile, created = Profile.objects.get_or_create(user=user)

#	user_like, user_like_created = UserLike.objects.get_or_create(user=request.user)
#	do_i_like = False
#	if user in user_like.liked_users.all():
#		do_i_like = True

	

	#user = get_object_or_404(User, username=username)
	#profile, created = Profile.objects.get_or_create(user=user)	
		
#	user = MyUser.objects.student_type()

	#project = get_object_or_404(Project, id=id)
#	project = Project.objects.get(slug=slug)
#	user_like, created = ProjectLike.objects.get_or_create(project=project)
#	do_i_like = False
#	if user == request.user:
#		if user in user_like.liked_users.all():
#			do_i_like = True

#	context = {
#		"do_i_like": do_i_like,
#				}
#	return render(request, "projects/project_detail.html", context)



#def get_context_data(self, *args, **kwargs):
#		context = super(CheckoutView, self).get_context_data(*args, **kwargs)
#		user_can_continue = False
#		user_check_id = self.request.session.get("user_checkout_id")
#		if self.request.user.is_authenticated():
#			user_can_continue = True
#			user_checkout, created = UserCheckout.objects.get_or_create(email=self.request.user.email)
#			user_checkout.user = self.request.user
#			user_checkout.save()
#			context["client_token"] = user_checkout.get_client_token()
#			self.request.session["user_checkout_id"] = user_checkout.id
#		elif not self.request.user.is_authenticated() and user_check_id == None:
#			context["login_form"] = AuthenticationForm()
#			context["next_url"] = self.request.build_absolute_uri()
#		else:
#			pass
#
#		if user_check_id != None:
#			user_can_continue = True
#			if not self.request.user.is_authenticated(): #GUEST USER
#				user_checkout_2 = UserCheckout.objects.get(id=user_check_id)
#				context["client_token"] = user_checkout_2.get_client_token()
		



		#if self.get_cart() is not None:
#		context["order"] = self.get_order()
#		context["user_can_continue"] = user_can_continue
#		context["form"] = self.get_form()
#		return context











