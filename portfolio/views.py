from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from projects.models import Project
from userprofiles.models import Profile
from .forms import PostForm
from django.core.urlresolvers import reverse


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from people.models import MyUser

MyUser = get_user_model()



#class CompanyPortfolioListView(ListView):
 #   model = Project
  #  template_name = 'companies/company_profile.html'
   # paginate_by = 3

   # def get_context_data(self, *args, **kwargs):

	#	posts = Project.objects.filter(user_company=user)
	#	context = super(CompanyPortfolioListView, self).get_context_data(*args, **kwargs)
	#	context["posts"] = posts
	#	return context



#def get_context_data(self, **kwargs):
 #       context = super(LocationDetailView, self).get_context_data(**kwargs)
  #      location = coremodels.Location.objects.get(id=self.kwargs['pk'])
   #     if self.request.user.is_authenticated():
    #        user_reviews = coremodels.Review.objects.filter(location=location, user=self.request.user)
     #       if user_reviews.count() > 0:
      #          context['user_review'] = user_reviews[0]
       #     else:
        #        context['user_review'] = None

        #return context




# Instead of using 'CompanyPortfolioListView', Used 'profile_view for company's user


class CompanyPortfolioCreateView(CreateView):
	template_name = "companies/post_form.html"
	form_class = PostForm


	def form_valid(self, form):
		form.instance.user_company = self.request.user
		#form.instance.added_by = self.request.user
		#form.instance.last_edited_by = self.request.user
		valid_form = super(CompanyPortfolioCreateView, self).form_valid(form)
		#messages.success(self.request, "Book created!")
		# send signals
		return valid_form


	def get_success_url(self):
		return reverse("project_list")




class CompanyPortfolioDetailView(DetailView):
	model = Project
	template_name = "portfolio/portfolio_detail.html"
	#context_object_name = 'project' : to have name instead of default one.




class CompanyPortfolioUpdateView(UpdateView):
	model = Project
	form_class = PostForm
	template_name = "companies/update_form.html"


	#def get_success_url(self):
	#	return reverse("profile_view")


# DeleteView
#class CompanyPortfolioDeleteView(DeleteView):
#	model = Project

	
class StudentPortfolioDetailView(DetailView):
	model = Project
	template_name = "portfolio/student_detail.html"






