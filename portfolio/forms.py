from django import forms
from projects.models import Project
from django.utils.text import slugify

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Project	
		fields = [
				'job_type',
				'project_title', 
				'company_overview',
				'position_name', 
				'position_summary',
				'salary_or_what_we_offer', 
				'deliverables', 
				'comments', 
				'how_to_submit', 
		]

	#clean title

	
	def clean_title(self):
			project_title = self.cleaned_data["project_title"]
			slug = slugify(project_title)
			try:
				project = Project.objects.get(slug=slug)
				raise forms.ValidationError("Title Already Exists. Please try a different one.")
			except Project.DoesNotExist:
				return title
			except:
				raise forms.ValidationError("Title Already Exists. Please try a different one.")



	 #def clean_username(self):
      #  username = self.cleaned_data.get("username")
       # try:
        #    exists = MyUser.objects.get(username=username)
         #   raise forms.ValidationError("This username is taken")
        #except MyUser.DoesNotExist:
        #    return username
        #except:
        #    raise forms.ValidationError("There was an error, please try again or contact us.")
